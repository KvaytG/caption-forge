# caption-forge

Automatically overlay perfectly fitted text on image

## 📚 Usage

```python
from PIL import Image
from captionforge import generate_caption_image

# Add text to image
generate_caption_image(
    pil_image=Image.open("input.png"),
    text="Example Text",
    font_path="OpenSans-Regular.ttf",
    to_hd=True,
    blur=True
).save("output.png")
```

## ⚙️ Installation
1. Clone the repository
```bash
git clone https://github.com/KvaytG/caption-forge.git
cd caption-forge
```
2. Create a virtual environment and install dependencies
```bash
python -m venv venv
.\venv\Scripts\activate  # Windows
pip install -e .
```

## 📜 License
caption-forge is licensed under the **[MIT license](https://opensource.org/license/mit)**.
