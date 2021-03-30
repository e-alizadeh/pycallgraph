import re
import sys

import pytest

from pycallgraph import Config
from pycallgraph.tracer import TraceProcessor

from . import calls


@pytest.fixture
def trace_processor(config):
    return TraceProcessor([], config)


def test_empty(trace_processor):
    sys.settrace(trace_processor.process)
    sys.settrace(None)

    assert trace_processor.call_dict == {}


def stdlib_trace(trace_processor, include_stdlib):
    trace_processor.config = Config(include_stdlib=include_stdlib)
    sys.settrace(trace_processor.process)
    re.match("asdf", "asdf")
    calls.one_nop()
    sys.settrace(None)
    return trace_processor.call_dict


def test_no_stdlib(trace_processor):
    assert "re.match" not in stdlib_trace(trace_processor, False)


def test_yes_stdlib(trace_processor):
    assert "re.match" in stdlib_trace(trace_processor, True)
