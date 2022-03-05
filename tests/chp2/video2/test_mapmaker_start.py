from scripts.chp2.video2.mapmaker_start import Point
from scripts.chp2.video2.mapmaker_start import Map
import pytest


def test_make_one_point():
    latitude = 50.4501
    longitude = 30.5234
    p1 = Point("Kiev", latitude, longitude)
    assert p1.latitudeAndLongitude() == (latitude, longitude)


def test_invalid_point_generation_negative_latitude():
    with pytest.raises(ValueError) as exp:
        Point("Graz", -955.34, 36.444)
        assert str(exp.value) == "Invalid latitude. -90 <= latitude <= 90"


def test_invalid_point_generation_positive_latitude():
    with pytest.raises(ValueError) as exp:
        Point("Graz", 955.34, 36.444)
        assert str(exp.value) == "Invalid latitude. -90 <= latitude <= 90"


def test_invalid_point_generation_negative_longitude():
    with pytest.raises(ValueError) as exp:
        Point("Graz", 55.34, -336.444)
        assert str(exp.value) == "Invalid longitude. -180 <= longitude <= 180"


def test_invalid_point_generation_positive_longitude():
    with pytest.raises(ValueError) as exp:
        Point("Graz", 55.34, 336.444)
        assert str(exp.value) == "Invalid longitude. -180 <= longitude <= 180"


def test_invalid_point_name_type():
    with pytest.raises(TypeError) as exp:
        notAName = 42
        Point(notAName, 55.34, 36.444)
        assert str(exp.value) == "Invalid type. city name type has to be a string"


def test_make_one_map():
    taipeiPoint = Point("Taipei", 25.105497, 121.597366)
    alicantePoint = Point("Alicante", 38.3460, 0.4907)
    aMap = Map()
    aMap.addPoint(taipeiPoint)
    aMap.addPoint(alicantePoint)
    assert aMap.has(taipeiPoint) and aMap.has(alicantePoint)


def test_invalid_point_not_stored_in_map():
    taipeiPoint = Point("Taipei", 25.105497, 121.597366)
    with pytest.raises(ValueError) as exp:
        Map().has(taipeiPoint)
        assert str(exp.value) == "Invalid point. Point isn't stored in map"