from datetime import datetime

from app.udaconnect.models import Location, Person
from app.udaconnect.schemas import (
    ConnectionSchema,
    LocationSchema,
    PersonSchema,
)
from flask import request
from flask_accepts import accepts, responds
from flask_restx import Namespace, Resource
from typing import Optional, List
import requests
from app.config import SERVICE_URL_CONNECTION, SERVICE_URL_LOCATION, SERVICE_URL_PERSON

DATE_FORMAT = "%Y-%m-%d"

api = Namespace("UdaConnect", description="Connections via geolocation.")  # noqa


# TODO: This needs better exception handling


@api.route("/locations")
@api.route("/locations/<location_id>")
@api.param("location_id", "Unique ID for a given Location", _in="query")
class LocationResource(Resource):
    @accepts(schema=LocationSchema)
    @responds(schema=LocationSchema)
    def post(self) -> Location:
        r = requests.post('http://' + SERVICE_URL_LOCATION + '/locations', data=request.get_json())
        return r.json()

    @responds(schema=LocationSchema)
    def get(self, location_id) -> Location:
        r = requests.get('http://' + SERVICE_URL_LOCATION + f'/locations/{location_id}')
        return r.json()


@api.route("/persons")
class PersonsResource(Resource):
    @accepts(schema=PersonSchema)
    @responds(schema=PersonSchema)
    def post(self) -> Person:
        r = requests.post('http://' + SERVICE_URL_PERSON + '/persons', data=request.get_json())
        return r.json()

    @responds(schema=PersonSchema, many=True)
    def get(self) -> List[Person]:
        r = requests.get('http://' + SERVICE_URL_PERSON + '/persons')
        return r.json()


@api.route("/persons/<person_id>")
@api.param("person_id", "Unique ID for a given Person", _in="query")
class PersonResource(Resource):
    @responds(schema=PersonSchema)
    def get(self, person_id) -> Person:
        r = requests.get('http://' + SERVICE_URL_PERSON + f'/persons/{person_id}')
        return r.json()


@api.route("/persons/<person_id>/connection")
@api.param("start_date", "Lower bound of date range", _in="query")
@api.param("end_date", "Upper bound of date range", _in="query")
@api.param("distance", "Proximity to a given user in meters", _in="query")
class ConnectionDataResource(Resource):
    @responds(schema=ConnectionSchema, many=True)
    def get(self, person_id) -> ConnectionSchema:
        r = requests.get('http://' + SERVICE_URL_CONNECTION + f'/persons/{person_id}', params=request.args)
        return r.json()
