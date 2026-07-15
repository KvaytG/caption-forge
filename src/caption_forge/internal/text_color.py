import numpy as np
from PIL.Image import Image


def _get_average_color(pil_image: Image) -> tuple[int, int, int]:
    if pil_image.width == 0 or pil_image.height == 0:
        return 0, 0, 0
    image = pil_image.convert('RGB')
    img_array: np.ndarray = np.array(image)
    avg_color: np.ndarray = img_array.mean(axis=(0, 1))
    return tuple(np.round(avg_color).astype(int))  # type: ignore[return-value]


def _get_contrast_color(avg_color: tuple[int, int, int]) -> tuple[int, int, int]:
    color_array = np.array(avg_color, dtype=np.float32)
    contrast_color = 255 - color_array
    mask: np.ndarray = contrast_color < 128
    contrast_color[mask] = np.maximum(0, contrast_color[mask] - 40)
    contrast_color[~mask] = np.minimum(255, contrast_color[~mask] + 40)
    return tuple(contrast_color.astype(int))  # type: ignore[return-value]


def get_text_color(pil_image: Image) -> tuple[int, int, int]:
    """ INTERNAL FUNCTION! """
    return _get_contrast_color(_get_average_color(pil_image))
