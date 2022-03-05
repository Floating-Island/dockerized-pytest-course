from scripts.chp2.video2.mapmaker_start import Point
import pytest

def test_make_one_point():
    latitude = 50.4501
    longitude = 305234
    p1 = Point("Kiev", latitude, longitude)
    assert p1.latitudeAndLongitude() == (latitude, longitude)

def test_invalid_point_generation():
    with pytest.raises(Exception) as exp:
        Point("Graz", -955.34, 36.444)

