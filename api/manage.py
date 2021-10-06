import os
import unittest

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from faker import Faker
import uuid

from app import api_blueprint
from app.main import create_app, db
from app.main.model import book, metadata, bookprocess, readingprogress 
from app.main.errors import errors

app = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')
app.register_blueprint(api_blueprint, url_prefix="/v1")
app.register_blueprint(errors)

app.app_context().push()

manager = Manager(app)

migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)


@manager.command
def run():
    app.run()


@manager.command
def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover('app/test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1

@manager.command
def seed():
    """Seed database"""
    fake = Faker()
    Faker.seed(0)

    for _ in range(50):
        num_pages = fake.pyint(1, 1000)

        instance = book.Book(
            cover_image = fake.file_name(category="image"),
            file_id = fake.uuid4(),
            num_pages = num_pages,
            book_type = book.BookType.comic,
            book_process = bookprocess.BookProcess(
                   error_code=0,
                   status=[bookprocess.ProcessStatus.running,
                           bookprocess.ProcessStatus.finished,
                           bookprocess.ProcessStatus.error
                       ][fake.pyint(0, 2)],
                ),
            reading_progress = readingprogress.ReadingProgress(
                    page = fake.pyint(1, num_pages),
                    read = fake.pybool() 
                ),
            meta = [
                    metadata.Metadata(
                            key = "title",
                            value = fake.sentence(nb_words=4),
                            data_type = metadata.DataType.string
                        )
                ]
        )
        db.session.add(instance)
        db.session.commit()


if __name__ == '__main__':
    manager.run()
