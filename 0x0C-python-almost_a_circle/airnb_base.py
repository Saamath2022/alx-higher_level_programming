#!/urs/bin/python3

from .base import base
with open("models/airbnb.py", "w") as f:
    f.write("""
from models.base import Base

class Airbnb(Base):
    def __init__(self, name, location, id=None):
        super().__init__(id)
        self.name = name
        self.location = location

    def get_info(self):
        return f"Name: {self.name}, Location: {self.location}"

if __name__ == '__main__':
    hotel = Airbnb("Hotel ABC", "New York")
    print(hotel.get_info())
""")
