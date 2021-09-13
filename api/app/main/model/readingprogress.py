from .. import db
import datetime
from sqlalchemy.sql import func

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
