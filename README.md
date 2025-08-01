# caption-forge

![Python 3.10](https://img.shields.io/badge/Python-3.10-blue?logo=python) ![MIT License](https://img.shields.io/badge/License-MIT-green) [![Sponsor](https://img.shields.io/badge/Sponsor-%E2%9D%A4-red)](https://kvaytg.ru/donate.php?lang=en)

Automatically overlay perfectly fitted text on image

## 📚 Usage

```python
from caption_forge import generate_caption_image
from PIL import Image

# Load image
image = Image.open("image.jpg")

# Generate text with default settings
result = generate_caption_image(
    pil_image=image,
    text="Привет, мир! Это пример текста в манге.",
    font_path="fonts/manga_font.ttf"
)
result.save("output_default.jpg")

# Advanced Customization
result_advanced = generate_caption_image(
    pil_image=image,
    text="Это продвинутый пример с настройками",
    font_path="fonts/bold_font.ttf",
    text_color=(30, 30, 30),
    initial_font_size=80,
    horizontal_margin_ratio=0.15,
    vertical_margin_ratio=0.1,
    blur=True,
    blur_radius=40,
    outline_color=(255, 255, 255),
    outline_width=2,
    align="left",
    line_spacing_coefficient=0.7
)
result_advanced.save("output_advanced.jpg")
```

## ⚙️ Installation
```bash
pip install git+https://github.com/KvaytG/caption-forge.git
```

## 📜 License
Licensed under the **[MIT](LICENSE.txt)** license.

This project uses open-source components. For license details see **[pyproject.toml](pyproject.toml)** and dependencies' official websites.
