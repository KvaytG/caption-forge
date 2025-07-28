from textwrap import wrap
from PIL import ImageDraw, ImageFont, ImageFilter
from PIL.Image import Image
from PIL.ImageFont import FreeTypeFont
import random
from .internal.text_color import get_text_color


def _calculate_font_spacing(font: FreeTypeFont, coefficient: float = 0.5) -> int:
    ascent, descent = font.getmetrics()
    return max(1, int((ascent + descent) * coefficient))


def _pil_word_wrap(
    pil_image: Image,
    xy_top_left: tuple[int, int],
    font_path: str,
    init_font_size: int,
    text: str,
    roi_width: int,
    roi_height: int,
    align: str
) -> tuple[str, int]:
    if not text.strip():
        return text, init_font_size

    font_size = init_font_size
    draw = ImageDraw.Draw(pil_image)

    def eval_metrics(txt: str, font_obj: FreeTypeFont) -> tuple[float, float]:
        spacing = _calculate_font_spacing(font_obj)
        bbox = draw.multiline_textbbox(xy=xy_top_left, text=txt, font=font_obj, align=align, spacing=spacing)
        return bbox[2] - bbox[0], bbox[3] - bbox[1]

    while font_size > 1:
        font = ImageFont.truetype(font_path, font_size)
        sample = text if len(text) <= 50 else ''.join(random.sample(text, 50))
        avg_char_width = font.getlength(sample) / len(sample)

        max_columns = max(1, min(len(text), int(roi_width / avg_char_width)))
        wrapped = '\n'.join(wrap(text, max_columns, break_long_words=False))
        w, h = eval_metrics(wrapped, font)

        if w <= roi_width and h <= roi_height:
            return wrapped, font_size

        if h > roi_height:
            font_size -= 1
            continue

        for cols in range(max_columns - 1, 0, -1):
            wrapped_try = '\n'.join(wrap(text, cols, break_long_words=False))
            w_try, h_try = eval_metrics(wrapped_try, font)

            if w_try <= roi_width and h_try <= roi_height:
                return wrapped_try, font_size
            if h_try > roi_height:
                break

        font_size -= 1

    fallback = '\n'.join(wrap(text, roi_width // 10, break_long_words=False))
    return fallback, 1


def generate_caption_image(
    pil_image: Image,
    text: str,
    font_path: str,
    text_color: tuple[int, int, int] | None = None,
    initial_font_size: int = 100,
    horizontal_margin_ratio: float = 0.2,
    vertical_margin_ratio: float = 0.1,
    blur: bool = False
) -> Image:
    width, height = pil_image.size

    if blur:
        pil_image = pil_image.filter(ImageFilter.GaussianBlur(50))

    max_width = int(width * (1 - horizontal_margin_ratio))
    max_height = int(height * (1 - vertical_margin_ratio))

    if text_color is None:
        text_color = get_text_color(pil_image)

    wrapped_text, font_size = _pil_word_wrap(
        pil_image,
        (0, 0),
        font_path,
        initial_font_size,
        text,
        max_width,
        max_height,
        align='center'
    )

    font = ImageFont.truetype(font_path, font_size)
    draw = ImageDraw.Draw(pil_image)
    spacing = _calculate_font_spacing(font)
    bbox = draw.multiline_textbbox((0, 0), wrapped_text, font=font, spacing=spacing, align="center")
    text_w, text_h = bbox[2] - bbox[0], bbox[3] - bbox[1]

    x = (width - text_w) / 2
    y = (height - text_h) / 2 - spacing / 2

    draw.multiline_text((x, y), wrapped_text, font=font, spacing=spacing, align="center", fill=text_color)
    return pil_image
