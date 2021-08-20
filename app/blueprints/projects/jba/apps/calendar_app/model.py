import datetime

from app.models import BaseModel
from app.models import db


class Event(BaseModel):
    __tablename__ = "events"

    id = db.Column(db.Integer, primary_key=True)
    event = db.Column(db.String(80), nullable=False)
    date = db.Column(db.Date, nullable=False)

    def __init__(self,
                 event: str,
                 _date: datetime.date):
        self.event = event
        self.date = _date
        super().__init__()

    def __repr__(self):
        return f"<Event {self.event} - {self.date}>"

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "event": self.event,
            "date": str(self.date)
        }

    @classmethod
    def find_by_event(cls, event: str) -> "Event":
        return cls.query.filter_by(event=event).first()

    @classmethod
    def find_all_by_date(cls, _date: datetime.date) -> list["Event"]:
        return cls.query.filter_by(date=_date).all()

    @classmethod
    def find_all_by_interval(cls,
                             start_time: datetime.date,
                             end_time: datetime.date) -> list["Event"]:
        # filter_by uses keyword arguments, whereas filter allows pythonic
        # filtering arguments like filter(User.name=="john")
        return Event.query.filter(Event.date <= end_time,
                                  Event.date >= start_time)
