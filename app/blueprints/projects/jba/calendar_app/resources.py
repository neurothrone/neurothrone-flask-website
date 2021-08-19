import datetime

from flask import abort
from flask_restful import Resource
from flask_restful import reqparse
from flask_restful import inputs

from app.blueprints.projects.jba.calendar_app.model import Event


class CreateEvent(Resource):
    _parser = reqparse.RequestParser()

    @classmethod
    def post(cls):
        cls._parser.add_argument(
            "event",
            type=str,
            help="The event name is required!",
            required=True,
            location="form"
        )
        cls._parser.add_argument(
            "date",
            type=inputs.date,
            help="The event date with the correct format is required! The correct format is YYYY-MM-DD!",
            required=True,
            location="form"
        )

        args = cls._parser.parse_args()
        event = args["event"]
        _date = args["date"]

        if Event.find_by_event(event):
            return {
                "message": "That event exists already."
            }

        new_event = Event(event=event,
                          _date=_date)
        new_event.save_to_db()

        # inputs.date returns a datetime object, thus you can access the date() method
        return {
            "message": "The event has been added!",
            "event": new_event.event,
            "date": str(new_event.date)
        }


class Events(Resource):
    _parser = reqparse.RequestParser()

    @classmethod
    def get(cls):
        cls._parser.add_argument(
            "start_time",
            type=inputs.date,
            help="The date with the correct format is required! The correct format is YYYY-MM-DD!",
            required=False,
        )
        cls._parser.add_argument(
            "end_time",
            type=inputs.date,
            help="The date with the correct format is required! The correct format is YYYY-MM-DD!",
            required=False,
        )

        if not Event.find_all():
            return {
                "message": "There are no events."
            }

        args = cls._parser.parse_args()
        start_time = args["start_time"]
        end_time = args["end_time"]

        if start_time and end_time:
            events = Event.find_all_by_interval(start_time=start_time,
                                                end_time=end_time)
            return Event.all_to_dict(items=events)

        # return all events from the database
        return Event.all_to_dict()


class EventsToday(Resource):
    @classmethod
    def get(cls):
        today = datetime.date.today()
        events = Event.find_all_by_date(_date=today)

        if not events:
            return {"data": "There are no events for today!"}

        # return all events for today
        return Event.all_to_dict(items=events)


class EventByID(Resource):
    @classmethod
    def get(cls, event_id: int):
        if (event := Event.find_by_id(event_id)) is None:
            abort(404, "The event doesn't exist!")
        return event.to_dict()

    @classmethod
    def delete(cls, event_id: int):
        if (event := Event.find_by_id(event_id)) is None:
            abort(404, "The event doesn't exist!")
        event.delete_from_db()
        return {"message": "The event has been deleted!"}
