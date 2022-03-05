import os
import pytest

from scripts import data_processor, data_aggregator


@pytest.fixture(scope="module")
def city_list_location():
    return 'tests/resources/cities/'


@pytest.fixture(scope="module")
def process_data(city_list_location):
    files = os.listdir(city_list_location)

    def _specify_type(file_name_or_type):
        for file in files:
            if file_name_or_type in file:
                if '.json' in file_name_or_type:
                    data = data_processor.json_reader(city_list_location + file)
                else:
                    data = data_processor.csv_reader(city_list_location + file)

        return data

    yield _specify_type


@pytest.mark.parametrize("country,statToUse,expectedValue", [
    ('Andorra', 'Mean', 1641.42),
    ('Andorra', 'Median', 1538.02),
    ('Argentina', 'Median', 125.0)
])
def test_altitude_stat_per_country(process_data, country, statToUse, expectedValue):
    data = process_data(file_name_or_type="clean_map.csv")
    country_stat_res = data_aggregator.altitude_stat_per_country(data, country, statToUse)

    assert country_stat_res == {'Country': country, statToUse: expectedValue}
