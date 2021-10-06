from .. import db
import datetime
from enum import Enum
from sqlalchemy.dialects.postgresql import ENUM

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
