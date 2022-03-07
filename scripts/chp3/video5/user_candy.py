class User():
    def __init__(self, height, favoriteColor):
        self._height = height
        self._favoriteColor = favoriteColor

    def height(self):
        return self._height

    def favoriteColor(self):
        return self._favoriteColor


class Award():
    @staticmethod
    def giveCandyTo(aUser):
        if aUser.height() < 2.00:
            return 'chocolate'
        if aUser.height() >= 2.00:
            return 'marshmallow'
