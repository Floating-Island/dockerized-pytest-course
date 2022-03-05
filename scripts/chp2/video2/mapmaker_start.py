class Point():
    def __init__(self, cityName, latitude, longitude):#__init__ denotes the class constructor
        self._cityName = cityName# _ indicates a private member variable
        if (latitude < -90):
            raise ValueError("Invalid latitude. Value must be greater or equal than -90")
        self._latitude = latitude
        self._longitude = longitude
    
    def latitudeAndLongitude(self):
        return (self._latitude, self._longitude)