from pathlib import Path
import time

import numpy as np
import open3d as o3d
import viser


def main() -> None:
    base_dir = Path(__file__).resolve().parent.parent
    pcd_path = base_dir / "data" / "cube_points.pcd"
    pcd = o3d.io.read_point_cloud(str(pcd_path))
    if pcd.is_empty():
        raise RuntimeError(f"Failed to load point cloud: {pcd_path}")

    points = np.asarray(pcd.points, dtype=np.float32)
    colors = np.tile(np.array([[0.2, 0.6, 1.0]], dtype=np.float32), (points.shape[0], 1))

    server = viser.ViserServer(port=8080)
    server.scene.add_frame("world", axes_length=0.2)
    server.scene.add_point_cloud("world/pcd", points=points, colors=colors, point_size=0.03)

    print("Viser running at http://localhost:8080")
    print("Press Ctrl+C to stop.")
    try:
        while True:
            time.sleep(1.0)
    except KeyboardInterrupt:
        print("\nExit.")


if __name__ == "__main__":
    main()
