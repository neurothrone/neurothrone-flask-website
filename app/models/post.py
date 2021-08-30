from typing import Generic
from typing import TypeVar

from app.models import BaseModel
from app.models import db

T = TypeVar("T", bound="Post")


class Post(BaseModel, Generic[T]):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), index=True)
    body = db.Column(db.String(400))

    def __init__(self, title: str, body: str) -> None:
        self.title = title
        self.body = body
        super().__init__()

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.title}, {self.body})"

    @property
    def date(self) -> str:
        return f"{self.created_on.strftime('%b %d %Y %H:%M:%S')}"

    def to_dict(self) -> dict:
        return {
                   "id": self.id,
                   "title": self.title,
                   "body": self.body
               } | super().to_dict()

    @classmethod
    def find_by_title(cls, title: str) -> T:
        return cls.query.filter_by(title=title).first()
