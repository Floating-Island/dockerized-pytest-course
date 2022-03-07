import pytest

from scripts.chp3.video5.user_candy import User
from scripts.chp3.video5.user_candy import Award


@pytest.mark.parametrize("height, favoriteColor", [
    (1.70, 'red'),
    (2.90, 'yellow')
])
def test_create_user(height, favoriteColor):
    aUser = User(height, favoriteColor)
    assert aUser.height() == height and aUser.favoriteColor() == favoriteColor


@pytest.mark.parametrize("height, favoriteColor, expectedAward", [
    (1.70, 'red', 'chocolate'),
    (2.90, 'yellow', 'marshmallow')
])
def test_award_user(height, favoriteColor, expectedAward):
    aUser = User(height, favoriteColor)
    candy = Award.giveCandyTo(aUser)
    assert candy == expectedAward
