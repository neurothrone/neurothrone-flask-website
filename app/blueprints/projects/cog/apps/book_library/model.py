from app.models import BaseModel
from app.models import db


class BookCategory:
    READING = "reading"
    HAVE_READ = "have_read"
    WILL_READ = "will_read"


class Book(BaseModel):
    __tablename__ = "books"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    author = db.Column(db.String(120))
    category = db.Column(db.String(10))
    book_link = db.Column(db.String(120))
    image_link = db.Column(db.String(120))

    def __init__(self,
                 name: str,
                 author: str,
                 category: str = "",
                 book_link: str = "",
                 image_link: str = "") -> None:
        self.name = name
        self.author = author
        self.category = category
        self.book_link = book_link
        self.image_link = image_link
        super().__init__()

    @property
    def alt_text(self) -> str:
        return f"book cover for {self.name} by {self.author}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.name}, {self.author}, " \
               f"{self.category}, {self.book_link}, {self.image_link})'>"

    def __str__(self) -> str:
        return f"{self.name} by {self.author}"

    def update(self, data: dict[str, str]) -> None:
        self.name = data["name"]
        self.author = data["author"]
        self.category = data["category"]
        self.book_link = data["book_link"]
        self.image_link = data["image_link"]
        db.session.commit()

    def to_dict(self) -> dict:
        return {
                   "id": self.id,
                   "name": self.name,
                   "author": self.author,
                   "category": self.category,
                   "book_link": self.book_link,
                   "image_link": self.image_link,
                   "alt_text": self.alt_text,
               } | super().to_dict()

    @classmethod
    def find_by_name(cls, name: str) -> "Book":
        return cls.query.filter_by(name=name).first()

    @classmethod
    def find_by_author(cls, author: str) -> "Book":
        return cls.query.filter_by(author=author).first()
