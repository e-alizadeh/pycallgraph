import sys
from collections import defaultdict

import pytest

from pycallgraph.config import Config
from pycallgraph.tracer import TraceProcessor

from . import sample


@pytest.fixture(scope="module")
def config():
    return Config()


@pytest.fixture(scope="module")
def trace_processor(config):
    return TraceProcessor([], config)


def test_nop(trace_processor):
    sys.settrace(trace_processor.process)
    sample.nop()
    sys.settrace(None)
    computed_output = {k: v for k, v in trace_processor.call_dict.items()}
    expected_output = {"__main__": defaultdict(int, {"test.sample.nop": 1})}
    assert computed_output == expected_output


def test_one_nop(trace_processor):
    sys.settrace(trace_processor.process)
    sample.one_nop()
    sys.settrace(None)
    computed_output = {k: v for k, v in trace_processor.call_dict.items()}
    expected_output = {
        "__main__": defaultdict(int, {"test.sample.one_nop": 1}),
        "test.sample.one_nop": defaultdict(int, {"test.sample.nop": 1}),
    }
    assert computed_output == expected_output
