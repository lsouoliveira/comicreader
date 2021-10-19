from app import models
from app.exceptions import ResourceNotFound
from app.main.repository.book_repository import save, find, find_by_id
from app.main.readers import ReaderFactory
from app.main.util import file_utils

ALLOWED_EXTENSIONS = ['cbz']

BOOK_TYPE = {
    'cbz': models.BookType.comic
}

reader_factory = ReaderFactory() 

def save_book(book):
    return save(book)

def add_books(files):
    books_added = []
    errors = []

    for file in files:
        try:
            filename, file_ext = extract_extension(file)

            if not file_ext in ALLOWED_EXTENSIONS:
                raise FileNotSupported(file)
            
            # Create reader
            reader = reader_factory.create(file_ext) 

            if not reader:
                raise FileNotSupported(file_ext)

            image_name, image_data = reader.extract_cover()

            # Create thumbnail 
            _, image_ext = extract_extension(image_name)

            # Resize image
            # TODO

            thumbnail_id = "..." 
            thumbnail_filename = "{}.{}".format(thumbnail_id, image_ext)
            thumbnail_path = THUMBNAIL_FOLDER + thumbnail_filename

            with open(thumbnail_path, "wb") as f:
                f.write(thumbnail_data)

            # Create book entity

            book = models.Book(
                cover_image = thumbnail_path,
                file_id = "",
                num_pages = reader.count_pages(),
                book_type = BOOK_TYPE[file_ext],
                reading_progress = models.ReadingProgress(
                    page=1,
                    read=False
                ),
                meta = [
                    models.Metadata(
                        key = "title",
                        value = filename,
                        data_type = models.DataType.string
                    )
                ],
                book_process = models.BookProcess(
                    error_code = 0,
                    status = models.ProcessStatus.running
                )
            )

            books_added.append(book)
        except FileNotSupported as e:
            errors.append(e)
        except Exception as e:
            errors.append(InvalidFile(file))

    # save books
    # TODO

    return books_added, errors

def get_all_books():
    return find()

def get_book_by_id(id):
    book = find_by_id(id)
    
    if not book:
        raise ResourceNotFound(id)

    return book

def bookmark(id, page):
    book = get_book_by_id(id)

    book.reading_progress.page = page

    return save(book)

def mark_as_read(id, read):
    book = get_book_by_id(id)

    book.reading_progress.read = read

    return save(book)

