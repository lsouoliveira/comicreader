import os

from flask_migrate import MigrateCommand
from flask_script import Manager
from faker import Faker
import uuid
import unittest
import json

from app import create_app, db
from app import models

app = create_app()

manager = Manager(app)
manager.add_command('db', MigrateCommand)

@manager.command
def run():
    app.run(host="0.0.0.0", debug=True)

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

        instance = models.Book(
            cover_image = fake.file_name(category="image"),
            file_id = fake.uuid4(),
            num_pages = num_pages,
            book_type = models.BookType.comic,
            book_process = models.BookProcess(
                   error_code=0,
                   status=[models.ProcessStatus.running,
                           models.ProcessStatus.finished,
                           models.ProcessStatus.error
                       ][fake.pyint(0, 2)],
                ),
            reading_progress = models.ReadingProgress(
                    page = fake.pyint(1, num_pages),
                    read = fake.pybool() 
                ),
            meta = [
                    models.Metadata(
                            key = "title",
                            value = fake.sentence(nb_words=4),
                            data_type = models.DataType.string
                        )
                ]
        )
        db.session.add(instance)
        db.session.commit()

if __name__ == '__main__':
    manager.run()
