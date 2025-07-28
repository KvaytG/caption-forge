# caption-forge

![Python 3.10](https://img.shields.io/badge/Python-3.10-blue?logo=python) ![MIT License](https://img.shields.io/badge/License-MIT-green) [![Sponsor](https://img.shields.io/badge/Sponsor-%E2%9D%A4-red)](https://kvaytg.ru/donate.php?lang=en)

Automatically overlay perfectly fitted text on image

## 📚 Usage

```python
from PIL import Image
from caption_forge import generate_caption_image

# Add text to image
generate_caption_image(
    pil_image=Image.open("input.png"),
    text="Example Text",
    font_path="example-font.ttf",
    blur=True
).save("output.png")
```

## ⚙️ Installation
```bash
pip install git+https://github.com/KvaytG/caption-forge.git
```

## 📜 License
caption-forge is licensed under the **[MIT license](https://opensource.org/license/mit)**.

This project uses open-source components. For license details see **[pyproject.toml](pyproject.toml)** and dependencies' official websites.
