from imgtools import load_image, resize_image, convert_to_grayscale

def test_resize():
    img = load_image("tests/sample.jpg")
    resized = resize_image(img, (100, 100))
    assert resized.size == (100, 100)

def test_grayscale():
    img = load_image("tests/sample.jpg")
    gray = convert_to_grayscale(img)
    assert gray.mode == "L"
