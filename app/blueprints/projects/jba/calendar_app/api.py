from flask_restful import Api


def init_api_routes(api: Api):
    from app.blueprints.projects.jba.calendar_app.resources import CreateEvent
    api.add_resource(CreateEvent, "/event")

    from app.blueprints.projects.jba.calendar_app.resources import Events
    api.add_resource(Events, "/events")

    from app.blueprints.projects.jba.calendar_app.resources import EventByID
    api.add_resource(EventByID, "/event/<int:event_id>")

    from app.blueprints.projects.jba.calendar_app.resources import EventsToday
    api.add_resource(EventsToday, "/events/today")
