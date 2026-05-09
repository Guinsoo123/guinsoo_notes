from pathlib import Path

import numpy as np
import open3d as o3d
import rerun as rr
import time


def load_points() -> np.ndarray:
    base_dir = Path(__file__).resolve().parent.parent
    pcd_path = base_dir / "data" / "two_clusters.pcd"
    pcd = o3d.io.read_point_cloud(str(pcd_path))
    if pcd.is_empty():
        raise RuntimeError(f"Failed to load point cloud: {pcd_path}")
    return np.asarray(pcd.points, dtype=np.float32)


def main() -> None:
    rr.init("rerun_pointcloud_demo", spawn=True)

    points = load_points()
    rr.log("world/pcd", rr.Points3D(points, radii=0.01))

    rr.log(
        "world/robot_pose",
        rr.Transform3D(
            translation=[0.2, 0.1, 0.0],
            mat3x3=[[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]],
        ),
    )
    rr.log("world/robot_pose/axis", rr.Arrows3D(origins=[[0, 0, 0]], vectors=[[0.2, 0, 0]]))

    print("Logged point cloud and pose to Rerun. Viewer should open automatically.")
    print("Press Ctrl+C to exit.")
    try:
        while True:
            time.sleep(1.0)
    except KeyboardInterrupt:
        print("\nExit.")


if __name__ == "__main__":
    main()
