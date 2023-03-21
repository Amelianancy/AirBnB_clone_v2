#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel


class State(BaseModel, ):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref="state", cascade='all, delete')
    
    @property
    def cities(self):
        from models import storage
        all_cities = storage.all(City)
        return [city for city in all_cities.values() if city.state_id == self.id]
