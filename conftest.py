import json
import os.path

import pytest
from datetime import datetime


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    report_dir = "reports"
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    config.option.htmlpath = f'{report_dir}/reports_{now}.html'


@pytest.fixture(scope='session', autouse=True)
def setup_teardown():
    print("Starting Test")
    yield
    print("Ending Test")


@pytest.fixture()
def data_source():
    json_file = os.path.join(os.path.dirname(__file__), "data", "test_data.json")
    with open(json_file) as data:
        test_data = json.load(data)
    return test_data
