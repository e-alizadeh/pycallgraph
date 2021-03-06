import tempfile

import pytest

from pycallgraph import Config, PyCallGraph


@pytest.fixture(scope="module")
def pycg():
    return PyCallGraph()


@pytest.fixture(scope="module")
def config():
    return Config()


@pytest.fixture(scope="module")
def temp():
    return tempfile.mkstemp()[1]
