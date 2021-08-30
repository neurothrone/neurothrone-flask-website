from app.models.account import Account


class Admin(Account):
    __tablename__ = "admins"

    MAX_LENGTH = 400
