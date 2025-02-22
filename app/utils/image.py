from PIL import Image

def resize_image(image: Image.Image, size=(384, 384)) -> Image.Image:
    """Resize the image to the given size."""
    return image.resize(size)
