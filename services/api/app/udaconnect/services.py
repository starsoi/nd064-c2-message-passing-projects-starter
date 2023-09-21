import logging
from datetime import datetime, timedelta
from typing import Dict, List

from app import db
from geoalchemy2.functions import ST_AsText, ST_Point
from sqlalchemy.sql import text

logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger("udaconnect-api")
