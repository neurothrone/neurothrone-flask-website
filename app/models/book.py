from app.models import BaseModel
from app.models import db


class BookModel(BaseModel):
    __tablename__ = "books"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    author = db.Column(db.String(120))
    # category = db.Column(db.String(10))
    # book_link = db.Column(db.String(120))
    # image_link = db.Column(db.String(120))
    # TODO: image resource?
    # alt_text = db.Column(db.String(120))

    def __init__(self,
                 name: str,
                 author: str) -> None:
        self.name = name
        self.author = author
        super().__init__()

    def __repr__(self):
        return f"<Book '{self.name}' by '{self.author}'>"

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "author": self.author,
            "created_on": self.created_on,
            "updated_on": self.updated_on
        }

    # def __init__(self,
    #              name: str,
    #              category: str,
    #              book_link: str,
    #              image_link: str,
    #              alt_text: str) -> None:
    #     self.name = name
    #     self.category = category
    #     self.book_link = book_link
    #     self.image_link = image_link
    #     self.alt_text = alt_text
    #
    # def to_dict(self) -> dict:
    #     return {
    #         "id": self.id,
    #         "name": self.name,
    #         "category": self.category,
    #         "book_link": self.book_link,
    #         "image_link": self.image_link,
    #         "alt_text": self.alt_text,
    #         "created_on": self.created_on,
    #         "updated_on": self.updated_on
    #     }
