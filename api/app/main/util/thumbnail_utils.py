from PIL import Image
import io
from typing import Tuple

def save_to(image_data: bytes, path: str, size: Tuple[int, int]) -> None:
    img = Image.open(io.BytesIO(image_data)) 
    img_resized = img.resize(size, Image.NEAREST)
    img_resized.save(path)

