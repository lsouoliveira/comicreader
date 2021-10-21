from PIL import Image
import io

def save_to(image_data: bytearray, path: str, size: tuple[int, int]) -> None:
    img = Image.open(io.BytesIO(image_data)) 
    img_resized = img.resize(size, Image.NEAREST)
    img_resized.save(path)

