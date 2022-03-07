import pytest

from scripts.chp3.video5.user_candy import User


def test_create_user():
    height = 1.70
    favoriteColor = 'red'
    aUser = User(height, favoriteColor)
    assert aUser.height() == height and aUser.favoriteColor() == favoriteColor
