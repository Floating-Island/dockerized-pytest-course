class Point():
    def __init__(self, cityName, latitude, longitude):#__init__ denotes the class constructor
        self._cityName = cityName# _ indicates a private member variable
        if (latitude < -90) or (latitude > 90):
            raise ValueError("Invalid latitude. -90 <= latitude <= 90")
        if (longitude < -180) or (longitude > 180):
            raise ValueError("Invalid longitude. -180 <= longitude <= 180")
        self._latitude = latitude
        self._longitude = longitude
    
    def latitudeAndLongitude(self):
        return (self._latitude, self._longitude)