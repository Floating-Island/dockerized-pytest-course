from multiprocessing.sharedctypes import Value
from operator import truediv
import string


class Point():
    def __init__(self, cityName, latitude, longitude):#__init__ denotes the class constructor
        if not isinstance(cityName, str):
            raise TypeError("Invalid type. city name type has to be a string")
        self._cityName = cityName# _ indicates a private member variable
        if (latitude < -90) or (latitude > 90):
            raise ValueError("Invalid latitude. -90 <= latitude <= 90")
        if (longitude < -180) or (longitude > 180):
            raise ValueError("Invalid longitude. -180 <= longitude <= 180")
        self._latitude = latitude
        self._longitude = longitude
    
    def latitudeAndLongitude(self):
        return (self._latitude, self._longitude)


class Map():
    def __init__(self):
        self._cityPoints = set()
    
    def addPoint(self, aPoint):
        self._cityPoints.add(aPoint)

    def has(self, aPoint):
        if aPoint in self._cityPoints:
            return True
        else:
            raise ValueError("Invalid point. Point isn't stored in map")