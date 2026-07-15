
# caption-forge

[![US](https://kvaytg.ru/common/flags/us-21x16.svg) English](README.md) | ![RU](https://kvaytg.ru/common/flags/ru-21x16.svg) **Русский**

![Python 3.10](https://img.shields.io/badge/Python-3.10-blue?logo=python) ![PolyForm License](https://img.shields.io/badge/License-PolyForm-blue) [![Sponsor](https://img.shields.io/badge/Sponsor-%E2%9D%A4-red)](https://kvaytg.ru/donate.php?lang=ru)

Автоматическое наложение идеально подогнанного текста на изображение.

## 📚 Использование
```python
from caption_forge import generate_caption_image
from PIL import Image

# Загрузка изображения
image = Image.open("image.jpg")

# Генерация текста с настройками по умолчанию
result = generate_caption_image(
    pil_image=image,
    text="Пример текста",
    font_path="example-font.ttf"
)
result.save("output.jpg")
```

## 📥 Установка
```bash
pip install git+https://github.com/KvaytG/caption-forge.git
```

## 📝 Лицензия
Распространяется по лицензии **[PolyForm Noncommercial](LICENSE.md)**.

Проект использует компоненты с открытым исходным кодом. Сведения о лицензиях см. в **[pyproject.toml](pyproject.toml)** и на официальных ресурсах зависимостей.
