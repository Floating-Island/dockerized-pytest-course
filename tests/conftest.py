# a way of modularizing conftest which needs to disable pylint for unused imports:
# from utility.cities import city_list_location #pylint:disable-unused-import
# from utility.data_processing import process_data #pylint:disable-unused-import

"""
Note:
Fixtures with @pytest.fixture(scope="session", autouse=True) must remain in this file
"""
# another way of modularizing conftest, specifying the pytest_plugins (I think it's better than the first one)
pytest_plugins = [
   "tests.utility.cities",
   "tests.utility.data_processing",
]
