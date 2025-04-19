from PIL import Image, ImageFilter

def load_image(path):
    return Image.open(path)

def save_image(image, path):
    image.save(path)

def resize_image(image, size):
    return image.resize(size)

def convert_to_grayscale(image):
    return image.convert("L")

def apply_blur(image, radius=2):
    return image.filter(ImageFilter.GaussianBlur(radius))
