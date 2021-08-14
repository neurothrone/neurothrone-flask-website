from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash

from app.models import BaseModel

from app.models import db


class UserModel(BaseModel):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(120))
    email = db.Column(db.String(120), index=True, unique=True)

    def __init__(self, username, password, email) -> None:
        self.username = username
        self.password_hash = self._hash_password(password)
        self.email = email
        super().__init__()

    def __repr__(self):
        return f"<User '{self.username}'>"

    @staticmethod
    def _hash_password(password: str) -> str:
        return generate_password_hash(password)

    def is_password_valid(self, password: str) -> bool:
        return check_password_hash(self.password_hash, password)

    def to_dict(self) -> dict:
        return {
                   "id": self.id,
                   "username": self.username,
                   "email": self.email,
               } | super().to_dict()

    @classmethod
    def find_by_username(cls, username: str) -> "UserModel":
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_email(cls, email: str) -> "UserModel":
        return cls.query.filter_by(email=email).first()
