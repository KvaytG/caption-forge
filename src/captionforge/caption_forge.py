from textwrap import wrap
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from PIL.ImageFont import FreeTypeFont

_hd_size = (1920, 1080)


def _calculate_font_spacing(font: FreeTypeFont, coefficient: float = 0.5) -> int:
    bounding_box = font.getbbox("H")
    text_height = bounding_box[3] - bounding_box[1]
    spacing = max(1, int(text_height * coefficient))
    return spacing


def _pil_word_wrap(
        pil_image: Image,
        xy_top_left: tuple[int, int],
        font_path: str,
        init_font_size: int,
        text: str,
        roi_width: int,
        roi_height: int,
        align: str,
        spacing: int
):
    mutable_message = text
    font_size = init_font_size
    font = ImageFont.truetype(font_path, font_size)

    def eval_metrics(txt, font_obj):
        bbox = ImageDraw.Draw(pil_image).multiline_textbbox(
            xy=xy_top_left,
            text=txt,
            font=font_obj,
            align=align,
            spacing=spacing
        )
        return bbox[2] - bbox[0], bbox[3] - bbox[1]

    while font_size > 1:
        font = font.font_variant(size=font_size)
        width, height = eval_metrics(mutable_message, font)
        if height > roi_height:
            font_size -= 1
            mutable_message = text
        elif width > roi_width:
            columns = len(mutable_message)
            while columns > 0:
                columns -= 1
                if columns == 0:
                    break
                mutable_message = '\n'.join(
                    wrap(text, columns, break_long_words=False))
                wrapped_width, _ = eval_metrics(mutable_message, font)
                if wrapped_width <= roi_width:
                    break
            if columns < 1:
                font_size -= 1
                mutable_message = text
        else:
            break
    return mutable_message, font_size


def generate_caption(
        image_path: str,
        output_path: str,
        text: str,
        font_path: str,
        initial_font_size: int = 1000,
        horizontal_margin_ratio: float = 0.2,
        vertical_margin_ratio: float = 0.1,
        to_hd: bool = False,
        blur: bool = False
):
    pil_image = Image.open(image_path)
    if to_hd:
        pil_image = pil_image.resize(_hd_size)
    width, height = pil_image.size
    if blur:
        pil_image = pil_image.filter(ImageFilter.GaussianBlur(50))

    max_width = int(width * (1 - horizontal_margin_ratio))
    max_height = int(height * (1 - vertical_margin_ratio))

    draw = ImageDraw.Draw(pil_image)
    initial_font = ImageFont.truetype(font_path, initial_font_size)
    initial_spacing = _calculate_font_spacing(initial_font)

    wrapped_text, font_size = _pil_word_wrap(
        pil_image,
        (0, 0),
        font_path,
        initial_font_size,
        text,
        max_width,
        max_height,
        align='center',
        spacing=initial_spacing
    )

    font = ImageFont.truetype(font_path, font_size)
    spacing = _calculate_font_spacing(font)
    bbox = draw.multiline_textbbox((0, 0), wrapped_text, font=font, spacing=spacing)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    x = (width - text_width) / 2
    y = (height - text_height) / 2 - bbox[1]

    shadow_offset = 5
    draw.multiline_text(
        (x + shadow_offset, y + shadow_offset),
        wrapped_text,
        font=font,
        spacing=spacing,
        align="center",
        fill="black"
    )
    draw.multiline_text(
        (x, y),
        wrapped_text,
        font=font,
        spacing=spacing,
        align="center",
        fill="white"
    )
    pil_image.save(output_path)
