from app import db
from datetime import datetime
class Product:
    def _init_(self, product_id):
        self.product_id = product_id

class Location:
    def _init_(self, location_id):
        self.location_id = location_id

class ProductMovement:
    def _init_(self, movement_id, timestamp, from_location, to_location, product_id, qty):
        self.movement_id = movement_id
        self.timestamp = timestamp
        self.from_location = from_location
        self.to_location = to_location
        self.product_id = product_id
        self.qty = qty