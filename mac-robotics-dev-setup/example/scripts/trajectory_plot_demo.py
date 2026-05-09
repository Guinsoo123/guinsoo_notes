from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main() -> None:
    base_dir = Path(__file__).resolve().parent.parent
    csv_path = base_dir / "data" / "trajectory_xy.csv"

    data = np.genfromtxt(csv_path, delimiter=",", names=True)
    t = data["t"]
    x = data["x"]
    y = data["y"]

    fig, ax = plt.subplots(1, 2, figsize=(10, 4))

    ax[0].plot(x, y, marker="o")
    ax[0].set_title("XY trajectory")
    ax[0].set_xlabel("x")
    ax[0].set_ylabel("y")
    ax[0].grid(True, linestyle="--", alpha=0.4)
    ax[0].axis("equal")

    ax[1].plot(t, x, label="x(t)")
    ax[1].plot(t, y, label="y(t)")
    ax[1].set_title("Time series")
    ax[1].set_xlabel("t")
    ax[1].set_ylabel("value")
    ax[1].legend()
    ax[1].grid(True, linestyle="--", alpha=0.4)

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
