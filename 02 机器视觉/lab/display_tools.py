"""本课程的对比图排版工具，不包含图像处理算法。"""
from pathlib import Path
import math
import cv2
import matplotlib.pyplot as plt

def show_images(images, cols=2, save_to=None):
    fig, axes = plt.subplots(math.ceil(len(images) / cols), cols,
                             figsize=(cols * 4, math.ceil(len(images) / cols) * 4),
                             squeeze=False)
    for ax, (title, image) in zip(axes.flat, images.items()):
        if image.ndim == 2:
            ax.imshow(image, cmap="gray", vmin=0, vmax=255)
        else:
            ax.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        ax.set_title(title)
        ax.axis("off")
    for ax in list(axes.flat)[len(images):]:
        ax.axis("off")
    fig.tight_layout()
    if save_to:
        path = Path("outputs") / save_to
        path.parent.mkdir(parents=True, exist_ok=True)
        fig.savefig(path, dpi=120, bbox_inches="tight")
    plt.show()
    plt.close(fig)
