import os
import json
import threading
from kafka import KafkaConsumer

from app import create_app
from app.location.services import LocationService
from app.config import SERVICE_URL_KAFKA

app = create_app(os.getenv("FLASK_ENV") or "test")

kafka_consumer = KafkaConsumer('udaconnect-location', bootstrap_servers=SERVICE_URL_KAFKA)

def kafka_worker():
    print('kafka worker started.')
    for message in kafka_consumer:
        print(f'new message: {message}')
        with app.app_context():
            LocationService.create(json.loads(message.decode('utf-8')))


if __name__ == "__main__":
    t = threading.Thread(target=kafka_worker)
    t.start()
    app.run(debug=True)
