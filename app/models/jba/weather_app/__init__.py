from app.models import BaseModel
from app.models import db


class CityModel(BaseModel):
    __tablename__ = "cities"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True, nullable=False)
    current_temp = db.Column(db.Integer, nullable=False)
    current_state = db.Column(db.String(30), default="Unknown")

    def __init__(self, name: str,
                 current_temp: int,
                 current_state: str) -> None:
        self.name = name
        self.current_temp = current_temp
        self.current_state = current_state
        super().__init__()

    def __repr__(self) -> str:
        return f"<City {self.id} : {self.name} : {self.current_temp} : {self.current_state}>"
