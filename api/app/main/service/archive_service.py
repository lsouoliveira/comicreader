from app.models import BookFormat
from app.main.parsers import CbzParser, Parser, ParserFactory

def extract_archive(path: str, to: str, book_format: BookFormat) -> None:
    parser_factory = ParserFactory()
    parser = parser_factory.create(book_format)

    if parser is None:
        raise Exception()

    with open(path, "rb") as f:
        parser.read(f.read())

        parser.extract_to(to)
