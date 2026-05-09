from pathlib import Path
import time

import meshcat
import meshcat.geometry as g
import meshcat.transformations as tf
import numpy as np
import open3d as o3d


def main() -> None:
    base_dir = Path(__file__).resolve().parent.parent
    pcd_path = base_dir / "data" / "two_clusters.pcd"

    pcd = o3d.io.read_point_cloud(str(pcd_path))
    if pcd.is_empty():
        raise RuntimeError(f"Failed to load point cloud: {pcd_path}")

    points = np.asarray(pcd.points, dtype=np.float32).T
    colors = np.tile(np.array([[0.2], [0.9], [0.3]], dtype=np.float32), (1, points.shape[1]))

    vis = meshcat.Visualizer().open()
    vis["world/points"].set_object(g.PointCloud(position=points, color=colors, size=0.02))
    vis["world/ref_box"].set_object(g.Box([0.15, 0.15, 0.15]))
    vis["world/ref_box"].set_transform(tf.translation_matrix([0.5, 0.0, 0.0]))

    print("MeshCat opened in browser.")
    print("Press Ctrl+C to stop.")
    try:
        while True:
            time.sleep(1.0)
    except KeyboardInterrupt:
        print("\nExit.")


if __name__ == "__main__":
    main()
