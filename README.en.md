
# caption-forge

![Python 3.10](https://img.shields.io/badge/Python-3.10-blue?logo=python) ![MIT License](https://img.shields.io/badge/License-MIT-green) [![Sponsor](https://img.shields.io/badge/Sponsor-%E2%9D%A4-red)](https://kvaytg.ru/donate.php?lang=en)

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
Licensed under the **[MIT](LICENSE.txt)** license.

This project uses open-source components. For license details see **[pyproject.toml](pyproject.toml)** and dependencies' official websites.
