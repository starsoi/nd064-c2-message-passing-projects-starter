from app.person.models import Connection, Location, Person  # noqa
from app.person.schemas import ConnectionSchema, LocationSchema, PersonSchema  # noqa


def register_routes(api, app, root="api"):
    from app.person.controllers import api as udaconnect_api

    api.add_namespace(udaconnect_api, path=f"/{root}")
