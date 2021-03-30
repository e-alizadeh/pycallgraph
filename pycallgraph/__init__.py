"""
Python Call Graph is a library and command line tool that visualises the flow
of your Python application.

See http://pycallgraph.slowchop.com/ for more information.
"""
import pathlib

ROOT_DIR: pathlib.Path = pathlib.Path(__file__).parent
TOP_DIR: pathlib.Path = ROOT_DIR.parent

from . import decorators
from .color import Color, ColorException
from .config import Config
from .decorators import trace
from .exceptions import PyCallGraphException
from .globbing_filter import GlobbingFilter
from .grouper import Grouper
from .metadata import (
    __author__,
    __copyright__,
    __credits__,
    __email__,
    __license__,
    __url__,
    __version__,
)
from .pycallgraph import PyCallGraph
from .util import Util
