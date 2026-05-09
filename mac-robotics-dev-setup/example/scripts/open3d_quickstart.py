from pathlib import Path

import open3d as o3d


def main() -> None:
    base_dir = Path(__file__).resolve().parent.parent
    pcd_path = base_dir / "data" / "cube_points.pcd"

    pcd = o3d.io.read_point_cloud(str(pcd_path))
    if pcd.is_empty():
        raise RuntimeError(f"Failed to load point cloud: {pcd_path}")

    pcd.paint_uniform_color([0.2, 0.7, 0.9])
    print(f"Loaded: {pcd_path}")
    print(f"Point count: {len(pcd.points)}")
    print("Close the Open3D window to exit.")

    o3d.visualization.draw_geometries(
        [pcd],
        window_name="Open3D Quickstart",
        width=960,
        height=720,
    )


if __name__ == "__main__":
    main()
