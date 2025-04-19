# imgtools

Um pacote simples para processamento de imagens usando Pillow.

## Instalação

```bash
pip install imgtools
```

## Exemplo de uso

```python
from imgtools import load_image, resize_image, save_image

img = load_image("foto.jpg")
img = resize_image(img, (300, 300))
save_image(img, "foto_redimensionada.jpg")
```
