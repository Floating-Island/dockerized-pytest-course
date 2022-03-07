import pytest

from scripts.chp3.video5.user_candy import User


@pytest.mark.parametrize("height, favoriteColor", [
    (1.70, 'red'),
    (2.90, 'yellow')
])
def test_create_user(height, favoriteColor):
    aUser = User(height, favoriteColor)
    assert aUser.height() == height and aUser.favoriteColor() == favoriteColor
