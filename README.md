
# caption-forge

![US](https://kvaytg.ru/common/flags/us-21x16.svg) **English** | [![RU](https://kvaytg.ru/common/flags/ru-21x16.svg) Русский](README.ru.md)

![Python 3.10](https://img.shields.io/badge/Python-3.10-blue?logo=python) ![PolyForm License](https://img.shields.io/badge/License-PolyForm-blue) [![Sponsor](https://img.shields.io/badge/Sponsor-%E2%9D%A4-red)](https://kvaytg.ru/donate.php?lang=en)

Automatically overlay perfectly fitted text on image.

## 📚 Usage

```python
from caption_forge import generate_caption_image
from PIL import Image

# Load image
image = Image.open("image.jpg")

# Generate text with default settings
result = generate_caption_image(
    pil_image=image,
    text="Example Text",
    font_path="example-font.ttf"
)
result.save("output.jpg")
```

## 📥 Installation
```bash
pip install git+https://github.com/KvaytG/caption-forge.git
```

## 📝 License
Licensed under the **[PolyForm Noncommercial](LICENSE.md)** license.

This project uses open-source components. For license details see **[pyproject.toml](pyproject.toml)** and dependencies' official websites.
