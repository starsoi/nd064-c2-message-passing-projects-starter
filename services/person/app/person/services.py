import logging
from datetime import datetime, timedelta
from typing import Dict, List

from app import db
from app.person.models import Person
from geoalchemy2.functions import ST_AsText, ST_Point
from sqlalchemy.sql import text

from app.protos import person_pb2
from app.protos import person_pb2_grpc

logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger("person-service")


class PersonService(person_pb2_grpc.PersonServiceServicer):
    app = None

    @staticmethod
    def create(person: Dict) -> Person:
        new_person = Person()
        new_person.first_name = person["first_name"]
        new_person.last_name = person["last_name"]
        new_person.company_name = person["company_name"]

        db.session.add(new_person)
        db.session.commit()

        return new_person

    @staticmethod
    def retrieve(person_id: int) -> Person:
        person = db.session.query(Person).get(person_id)
        return person

    @staticmethod
    def retrieve_all() -> List[Person]:
        return db.session.query(Person).all()

    def RetreaveAll(self, request, context):
        with PersonService.app.app_context():
            query_results = PersonService.retrieve_all()
        results = [{'id': person.id, 'first_name': person.first_name, 'last_name': person.last_name, 'company_name': person.company_name} for person in query_results]
        return person_pb2.Persons(persons=results)

