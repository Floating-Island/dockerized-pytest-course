class Point():
    def __init__(self, cityName, latitude, longitude):#__init__ denotes the class constructor
        self._cityName = cityName# _ indicates a private member variable
        self._latitude = latitude
        self._longitude = longitude