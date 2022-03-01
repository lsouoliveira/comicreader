from abc import ABC, abstractmethod
import zipfile
import io
import os
from typing import Optional, Tuple

from werkzeug.utils import secure_filename

from app.main.util import file_utils 
from app.models import BookFormat

ALLOWED_COMIC_IMAGES_EXT = ["png", "jpg", "jpeg"]

class InvalidImageType(Exception):
    def __init__(self):
        super.__init__()

class Parser(ABC):
    @abstractmethod
    def read(self, data: bytes) -> None:
        pass

    @abstractmethod
    def get_cover(self) -> Tuple[str, bytes]:
        pass

    @abstractmethod
    def count_pages(self) -> int:
        pass

    @abstractmethod
    def extract_to(self, path: str) -> None:
        pass

"""
TODO: validate all images from zip file
"""
class CbzParser(Parser):
    file = None

    def read(self, data: bytes) -> None:
        self.file = io.BytesIO(data)

    def get_cover(self) -> Tuple[str, bytes]:
        with zipfile.ZipFile(self.file, 'r') as cbz:
            cover_file = self.get_first_file(cbz) 
            _, ext = file_utils.extract_extension(cover_file.name) 

            if not ext in ALLOWED_COMIC_IMAGES_EXT:
                raise InvalidImageType()

            return secure_filename(cover_file.name), cover_file.read_bytes() 

    def count_pages(self):
        with zipfile.ZipFile(self.file, 'r') as f:
            root_path = zipfile.Path(f)
            members = [root_path]

            num_pages = 0

            while len(members) > 0:
                member = members.pop(0)

                if member.is_file():
                    num_pages += 1
                    continue

                for m in member.iterdir():
                    members.append(m)

            return num_pages

    def extract_to(self, path: str) -> None:
        with zipfile.ZipFile(self.file, 'r') as f:
            root_path = zipfile.Path(f)
            members = [root_path]

            file_index = 1

            if not os.path.exists(path):
                os.mkdir(path)

            while len(members) > 0:
                member = members.pop(0)

                if member.is_file():
                    _, ext = file_utils.extract_extension(member.name) 

                    with open('{}/{}.{}'.format(path, file_index, ext), 'wb') as image_file:
                        image_file.write(member.read_bytes())

                    file_index += 1
                    continue

                for m in member.iterdir():
                    members.append(m)

    def get_first_file(self, archive) -> zipfile.Path:
        root_path = zipfile.Path(archive)

        while root_path.is_dir():
            for member in root_path.iterdir():
                if member.is_dir():
                    root_path = member
                    break
                return member
        return root_path


class ParserFactory:
    def create(self, book_format: BookFormat) -> Optional[Parser]:
        if book_format == BookFormat.cbz:
            return CbzParser()

        return None
