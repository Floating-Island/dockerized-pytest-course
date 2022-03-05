from scripts.chp2.video2.mapmaker_start import Point

def test_make_one_point():
    latitude = 50.4501
    longitude = 305234
    p1 = Point("Kiev", latitude, longitude)
    assert p1.latitudeAndLongitude() == (latitude, longitude)