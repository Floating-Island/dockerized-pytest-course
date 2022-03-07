class User():
    def __init__(self, height, favoriteColor):
        self._height = height
        self._favoriteColor = favoriteColor

    def height(self):
        return self._height

    def favoriteColor(self):
        return self._favoriteColor
