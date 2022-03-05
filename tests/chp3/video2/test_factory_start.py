import os
import pytest
from scripts import data_processor


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

    yield _specify_type  # when called, we specify the filename or the type


@pytest.fixture(scope="function")
def check_processed_data():

    def _specify_data(processed_data):
        for row in processed_data:
            assert(isinstance(row['Country'], str))
            assert(isinstance(row['City'], str))
            assert(isinstance(row['State_Or_Province'], str))
            assert(isinstance(row['Lat'], float))
            assert(isinstance(row['Long'], float))
            assert(isinstance(row['Altitude'], float))

        # Basic processed_data checks
        assert len(processed_data) == 180  # We have collected 180 rows
        assert processed_data[0]['Country'] == 'Andorra'
        assert processed_data[106]['Country'] == 'Japan'
    yield _specify_data


def test_csv_reader_header_fields(process_data):
    """
    Happy Path test to make sure the processed data
    contains the right header fields
    """
    data = process_data(file_name_or_type='clean_map.csv')
    header_fields = list(data[0].keys())
    assert header_fields == [
            'Country',
            'City',
            'State_Or_Province',
            'Lat',
            'Long',
            'Altitude'
            ]


def test_csv_reader_data_contents(process_data, check_processed_data):
    """
    Happy Path Test to examine that each row
    had the appropriate data type per field
    """
    data = process_data(file_name_or_type='clean_map.csv')
    check_processed_data(processed_data=data)


def test_csv_reader_malformed_data_contents(process_data):
    """
    Sad Path Test
    """
    with pytest.raises(ValueError) as exp:
        process_data(file_name_or_type='malformed_map.csv')
    assert str(exp.value) == "could not convert string to float: 'not_an_altitude'"


def test_json_reader_data_contents(process_data, check_processed_data):
    """
    Happy Path Test to examine that each row
    had the appropriate data type per field
    """
    data = process_data(file_name_or_type='clean_map.json')
    check_processed_data(processed_data=data)


def test_json_reader_malformed_data_contents(process_data):
    """
    Sad Path Test
    """
    with pytest.raises(ValueError) as exp:
        process_data(file_name_or_type='malformed_map.json')
    assert str(exp.value) == "could not convert string to float: 'not_an_altitude'"
