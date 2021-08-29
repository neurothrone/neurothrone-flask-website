from app.models.account import Account


class User(Account):
    __tablename__ = "users"
