from app.models import BaseModel
from app.models import db


class UserModel(BaseModel):
    __tablename__ = "users"

    username = db.Column(db.String(120), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)

    def __init__(self, username, email) -> None:
        self.username = username
        self.email = email

    def to_dict(self) -> dict:
        return {
            "username": self.username,
            "email": self.email
        }
