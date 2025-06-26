from textwrap import wrap
from PIL import ImageDraw, ImageFont, ImageFilter
from PIL.Image import Image
from PIL.ImageFont import FreeTypeFont
from typing import Tuple, Optional
import random
from .internal.text_color import get_text_color

_hd_size = (1920, 1080)


def _calculate_font_spacing(font: FreeTypeFont, coefficient: float = 0.5) -> int:
    ascent, descent = font.getmetrics()
    text_height = ascent + descent
    spacing = max(1, int(text_height * coefficient))
    return spacing


def _pil_word_wrap(
        pil_image: Image,
        xy_top_left: Tuple[int, int],
        font_path: str,
        init_font_size: int,
        text: str,
        roi_width: int,
        roi_height: int,
        align: str
) -> Tuple[str, int]:
    if not text.strip():
        return text, init_font_size

    mutable_message = text
    font_size = init_font_size

    def eval_metrics(txt: str, font_obj: FreeTypeFont) -> Tuple[float, float]:
        spacing_here = _calculate_font_spacing(font_obj, 0.5)
        bbox = ImageDraw.Draw(pil_image).multiline_textbbox(
            xy=xy_top_left,
            text=txt,
            font=font_obj,
            align=align,
            spacing=spacing_here
        )
        return bbox[2] - bbox[0], bbox[3] - bbox[1]

    while font_size > 1:
        font = ImageFont.truetype(font_path, font_size)

        sample_length = min(50, len(text))
        sample = ''.join(random.sample(text, sample_length)) if len(text) > sample_length else text
        avg_char_width = font.getlength(sample) / len(sample)

        start_columns = max(1, min(len(text), int(roi_width / avg_char_width)))

        wrapped_text_try = '\n'.join(wrap(text, start_columns, break_long_words=False))
        w, h = eval_metrics(wrapped_text_try, font)

        if w <= roi_width and h <= roi_height:
            mutable_message = wrapped_text_try
            break

        if h > roi_height:
            font_size -= 1
            continue

        found = False
        for columns in range(start_columns - 1, 0, -1):
            wrapped_text_try = '\n'.join(wrap(text, columns, break_long_words=False))
            w_try, h_try = eval_metrics(wrapped_text_try, font)

            if w_try <= roi_width and h_try <= roi_height:
                mutable_message = wrapped_text_try
                found = True
                break

            if h_try > roi_height:
                break

        if found:
            break
        else:
            font_size -= 1

    if font_size == 1:
        # font = ImageFont.truetype(font_path, 1)
        wrapped_text_try = '\n'.join(wrap(text, roi_width // 10, break_long_words=False))
        mutable_message = wrapped_text_try

    return mutable_message, max(1, font_size)


def generate_caption_image(
        pil_image: Image,
        text: str,
        font_path: str,
        text_color: Optional[Tuple[int, int, int]] = None,
        initial_font_size: int = 100,
        horizontal_margin_ratio: float = 0.2,
        vertical_margin_ratio: float = 0.1,
        to_hd: bool = False,
        blur: bool = False) -> Image:
    if to_hd:
        pil_image = pil_image.resize(_hd_size)

    width, height = pil_image.size

    if blur:
        pil_image = pil_image.filter(ImageFilter.GaussianBlur(50))

    max_width = int(width * (1 - horizontal_margin_ratio))
    max_height = int(height * (1 - vertical_margin_ratio))
    draw = ImageDraw.Draw(pil_image)

    if text_color is None:
        text_color = get_text_color(pil_image)

    wrapped_text, font_size = _pil_word_wrap(
        pil_image=pil_image,
        xy_top_left=(0, 0),
        font_path=font_path,
        init_font_size=initial_font_size,
        text=text,
        roi_width=max_width,
        roi_height=max_height,
        align='center'
    )

    font = ImageFont.truetype(font_path, font_size)
    spacing = _calculate_font_spacing(font)
    bbox = draw.multiline_textbbox(
        xy=(0, 0),
        text=wrapped_text,
        font=font,
        spacing=spacing,
        align="center"
    )
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    x = (width - text_width) / 2
    y = (height - text_height) / 2

    draw.multiline_text(
        xy=(x, y),
        text=wrapped_text,
        font=font,
        spacing=spacing,
        align="center",
        fill=text_color
    )
    return pil_image
