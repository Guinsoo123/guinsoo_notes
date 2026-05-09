from pathlib import Path

import numpy as np
import open3d as o3d


def main() -> None:
    base_dir = Path(__file__).resolve().parent.parent
    source_path = base_dir / "data" / "two_clusters.pcd"

    source = o3d.io.read_point_cloud(str(source_path))
    if source.is_empty():
        raise RuntimeError(f"Failed to load point cloud: {source_path}")

    # 1) Voxel downsample.
    down = source.voxel_down_sample(voxel_size=0.03)

    # 2) Remove outliers.
    cleaned, _ = down.remove_statistical_outlier(nb_neighbors=6, std_ratio=1.0)
    cleaned.paint_uniform_color([0.2, 0.8, 0.3])

    # 3) Build a translated target and run ICP.
    target = o3d.geometry.PointCloud(cleaned)
    translation = np.array([0.15, -0.05, 0.08], dtype=np.float64)
    target.translate(translation)
    target.paint_uniform_color([0.9, 0.2, 0.2])

    result = o3d.pipelines.registration.registration_icp(
        source=cleaned,
        target=target,
        max_correspondence_distance=0.3,
        init=np.eye(4),
        estimation_method=o3d.pipelines.registration.TransformationEstimationPointToPoint(),
    )

    print("ICP fitness:", result.fitness)
    print("ICP inlier_rmse:", result.inlier_rmse)
    print("Estimated transform:\n", result.transformation)

    # Visualize before alignment.
    print("Showing before ICP...")
    o3d.visualization.draw_geometries(
        [cleaned, target],
        window_name="Before ICP (green=source, red=target)",
        width=960,
        height=720,
    )

    # Apply result and visualize after alignment.
    aligned = o3d.geometry.PointCloud(cleaned)
    aligned.transform(result.transformation)
    aligned.paint_uniform_color([0.2, 0.2, 1.0])

    print("Showing after ICP...")
    o3d.visualization.draw_geometries(
        [aligned, target],
        window_name="After ICP (blue=aligned source, red=target)",
        width=960,
        height=720,
    )


if __name__ == "__main__":
    main()
