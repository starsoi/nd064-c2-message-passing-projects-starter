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
import json
from app.config import SERVICE_URL_CONNECTION, SERVICE_URL_LOCATION, SERVICE_URL_PERSON, SERVICE_URL_KAFKA

DATE_FORMAT = "%Y-%m-%d"

api = Namespace("UdaConnect", description="Connections via geolocation.")  # noqa


from kafka import KafkaProducer
kafka_producer = KafkaProducer(bootstrap_servers=SERVICE_URL_KAFKA, acks='all')

# TODO: This needs better exception handling


@api.route("/locations")
@api.route("/locations/<location_id>")
@api.param("location_id", "Unique ID for a given Location", _in="query")
class LocationResource(Resource):
    @accepts(schema=LocationSchema)
    @responds(schema=LocationSchema)
    def post(self) -> Location:
        # r = requests.post('http://' + SERVICE_URL_LOCATION + '/api/locations', data=request.get_json())
        kafka_producer.send('udaconnect-location', request.get_data())
        kafka_producer.flush()
        schema = LocationSchema()
        return schema.load(request.get_json())

    @responds(schema=LocationSchema)
    def get(self, location_id) -> Location:
        r = requests.get('http://' + SERVICE_URL_LOCATION + f'/api/locations/{location_id}')
        schema = LocationSchema()
        return schema.load(r.json())


@api.route("/persons")
class PersonsResource(Resource):
    @accepts(schema=PersonSchema)
    @responds(schema=PersonSchema)
    def post(self) -> Person:
        print(request.get_json())
        r = requests.post('http://' + SERVICE_URL_PERSON + '/api/persons', json=request.get_json())
        return r.json()

    @responds(schema=PersonSchema, many=True)
    def get(self) -> List[Person]:
        r = requests.get('http://' + SERVICE_URL_PERSON + '/api/persons')
        return r.json()


@api.route("/persons/<person_id>")
@api.param("person_id", "Unique ID for a given Person", _in="query")
class PersonResource(Resource):
    @responds(schema=PersonSchema)
    def get(self, person_id) -> Person:
        r = requests.get('http://' + SERVICE_URL_PERSON + f'/api/persons/{person_id}')
        return r.json()


@api.route("/persons/<person_id>/connection")
@api.param("start_date", "Lower bound of date range", _in="query")
@api.param("end_date", "Upper bound of date range", _in="query")
@api.param("distance", "Proximity to a given user in meters", _in="query")
class ConnectionDataResource(Resource):
    @responds(schema=ConnectionSchema, many=True)
    def get(self, person_id) -> ConnectionSchema:
        r = requests.get('http://' + SERVICE_URL_CONNECTION + f'/api/persons/{person_id}/connection', params=request.args)
        schema = ConnectionSchema(many=True)
        result = schema.load(r.json())
        print(result)
        return result
