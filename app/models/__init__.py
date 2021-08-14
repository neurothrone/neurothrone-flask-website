from abc import abstractmethod
from datetime import datetime
from typing import Generic
from typing import Type
from typing import TypeVar

from app import db

T = TypeVar("T", bound="BaseModel")


class BaseModel(db.Model, Generic[T]):
    __abstract__ = True

    created_on = db.Column(db.DateTime,
                           default=datetime.utcnow())
    updated_on = db.Column(db.DateTime,
                           default=datetime.utcnow(),
                           onupdate=datetime.utcnow())

    def __init__(self):
        self.created_on = datetime.utcnow()
        self.updated_on = datetime.utcnow()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_id(cls: Type[T], _id: int) -> T:
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_by_name(cls: Type[T], name: str) -> T:
        return cls.query.filter_by(name=name).first()

    @classmethod
    def find_all(cls) -> T:
        return cls.query.all()

    @abstractmethod
    def to_dict(self) -> dict: ...

    @classmethod
    def all_to_dict(cls) -> list[T]:
        return [item.to_dict() for item in cls.find_all()]
