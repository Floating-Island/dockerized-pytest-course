from datetime import datetime
import pytest
from scripts.fitness_log import FitnessLog


@pytest.fixture(scope='module')
def tracker_activity():
    start_time = datetime(year=2017, month=1, day=1, hour=5, minute=12)
    end_time = datetime(year=2017, month=1, day=1, hour=5, minute=55)
    yield start_time, end_time


@pytest.fixture(scope='function')
def create_tracker(tracker_activity):
    fitness_tracker = FitnessLog()

    start_time, end_time = tracker_activity
    # breakpoint()
    fitness_tracker.log_activity("run", start_time, end_time)

    yield fitness_tracker


def test_add_valid_activities(create_tracker):
    fitness_tracker = create_tracker
    # breakpoint()
    activities = fitness_tracker.get_activities()

    assert len(activities) == 1
    assert activities[0][0] == 'run'


@pytest.fixture(scope='session')
def create_overlapping_times():
    overlapping_start_time = datetime(year=2017, month=1, day=1, hour=5, minute=14)
    overlapping_end_time = datetime(year=2017, month=1, day=1, hour=5, minute=53)

    return overlapping_start_time, overlapping_end_time


def test_add_invalid_activity(create_tracker, create_overlapping_times):
    fitness_tracker = create_tracker
    overlapping_start_time, overlapping_end_time = create_overlapping_times

    with pytest.raises(Exception) as exp:
        fitness_tracker.log_activity("run", overlapping_start_time, overlapping_end_time)

    assert str(exp.value) == ('A new activity must not conflict with a logged activity. ' +
                              'Please delete the old activity before proceeding')
"""
 TO DO: Add a new test.
 You can run the following to expose which test functions
 and paths are covered:

 pytest --cov scripts
"""


def test_delete_activity(create_tracker, tracker_activity):
    fitness_tracker = create_tracker
    start_time, end_time = tracker_activity
    fitness_tracker.delete_activity('run', start_time, end_time)
    activities = fitness_tracker.get_activities()

    assert len(activities) == 0


def test_invalid_entry(create_tracker, tracker_activity):
    fitness_tracker = create_tracker
    start_time, end_time = tracker_activity
    entry_validation = fitness_tracker.validate_entry(end_time, start_time)
    assert entry_validation is False


def test_non_overlapping_activity_empty_log(tracker_activity):
    fitness_tracker = FitnessLog()
    start_time, end_time = tracker_activity
    overlapping_entry = fitness_tracker.overlapping_entry(start_time, end_time)
    assert overlapping_entry is False
