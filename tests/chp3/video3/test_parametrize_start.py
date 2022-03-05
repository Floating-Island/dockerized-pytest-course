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


def test_average_atitude_per_country(process_data):
    data = process_data(file_name_or_type="clean_map.csv")
    andorran_avg_res = data_aggregator.atitude_stat_per_country(data, 'Andorra', 'Mean')

    assert andorran_avg_res == {'Country': 'Andorra', 'Mean': 1641.42}


def test_median_atitude_per_country(process_data):
    data = process_data(file_name_or_type="clean_map.csv")
    andorran_median_res = data_aggregator.atitude_stat_per_country(data, 'Andorra', 'Median')

    assert andorran_median_res == {'Country': 'Andorra', 'Median': 1538.02}
