# Caption Forge

Automatically overlay perfectly fitted text on image

## 📚 Usage
```python
from captionforge import generate_caption

# Add text to image with custom settings
generate_caption(
    image_path="input.jpg",
    output_path="output.jpg",
    text="Example Text",
    font_path="fonts/BebasNeue.ttf",
    to_hd=True,
    blur=True
)
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
Caption Forge is licensed under the **[MIT license](https://opensource.org/license/mit)**.
