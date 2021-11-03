from . import db
import datetime
from enum import Enum
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import ENUM

class BookType(Enum):
    comic = 1

class BookFormat(Enum):
    cbz = 1

class Book(db.Model):
    """ Book Model for storing book related details """
    __tablename__ = "book"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cover_image = db.Column(db.String(512), nullable=False)
    num_pages = db.Column(db.Integer, nullable=False, default=0)
    book_type = db.Column("book_type", ENUM(BookType, name="booktype_enum"), nullable=False)
    book_format = db.Column("book_format", ENUM(BookFormat, name="bookformat_enum"), nullable=False)
    meta = db.relationship("Metadata")
    book_process = db.relationship("BookProcess", uselist=False)
    reading_progress = db.relationship("ReadingProgress", uselist=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(
            db.DateTime,
            server_default=db.func.now(),
            server_onupdate=db.func.now()
    )

    def __repr__(self):
        return "<Book '{}'>".format(self.id)

class ProcessStatus(Enum):
    running = "running"
    finished = "finished"
    error = "error"

    def __str__(self):
        return self.value

class BookProcess(db.Model):
    """ BookProcess Model for storing book process related details """
    __tablename__ = "bookprocess"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    error_code = db.Column(db.Integer, nullable=False)
    status = db.Column(
            "status",
            ENUM(ProcessStatus,
            name="process_status_enum"),
            nullable=False
    )
    file_id = db.Column(db.String(512))
    book_id = db.Column(db.Integer, db.ForeignKey("book.id"))
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.func.now())
    updated_at = db.Column(
            db.DateTime,
            nullable=False,
            server_default=db.func.now(),
            server_onupdate=db.func.now()
    )

    def __repr__(self):
        return "<BookProcess '{}'>".format(self.id)

class DataType(Enum):
    string = "string"

    def __str__(self):
        return self.value

class Metadata(db.Model):
    """ Metadata Model for storing book metadata """
    __tablename__ = "metadata"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    key = db.Column(db.String(512), nullable=False)
    value = db.Column(db.String(512), nullable=False)
    data_type = db.Column("data_type", ENUM(DataType, name="datatype_enum"), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey("book.id"))
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.func.now())
    updated_at = db.Column(
            db.DateTime,
            nullable=False,
            server_default=db.func.now(),
            server_onupdate=db.func.now()
    )

    def __repr__(self):
        return "<Metadata '{}'>".format(self.id)

class ReadingProgress(db.Model):
    """ ReadingProgress Model for storing book reading progress """
    __tablename__ = "readingprogress"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    page = db.Column(db.Integer, nullable=False, default=1)
    read = db.Column(db.Boolean, nullable=False, default=False)
    book_id = db.Column(db.Integer, db.ForeignKey("book.id"))
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.func.now())
    updated_at = db.Column(
            db.DateTime,
            nullable=False,
            server_default=db.func.now(),
            server_onupdate=db.func.now()
    )

    def __repr__(self):
        return "<ReadingProgress '{}'>".format(self.id)
