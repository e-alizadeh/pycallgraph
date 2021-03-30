import os
import re
from abc import abstractmethod
from distutils.spawn import find_executable

from ..color import Color
from ..exceptions import PyCallGraphException


class Output(object):
    """Base class for all outputters."""

    def __init__(self, output_file="pycallgraph.png", **kwargs):
        self.processor = None
        self.output_file = output_file
        self.fp = None
        self.node_color_func = self.node_color
        self.edge_color_func = self.edge_color
        self.node_label_func = self.node_label
        self.edge_label_func = self.edge_label

        # Update the defaults with anything from kwargs
        [setattr(self, k, v) for k, v in kwargs.items()]

    def set_config(self, config):
        """
        This is a quick hack to move the config variables set in Config into
        the output module config variables.
        """
        for k, v in config.__dict__.items():
            if hasattr(self, k) and callable(getattr(self, k)):
                continue
            setattr(self, k, v)

    @staticmethod
    def node_color(node):
        value = float(node.time.fraction * 2 + node.calls.fraction) / 3
        return Color.hsv(value / 2 + 0.5, value, 0.9)

    @staticmethod
    def edge_color(edge):
        value = float(edge.time.fraction * 2 + edge.calls.fraction) / 3
        return Color.hsv(value / 2 + 0.5, value, 0.7)

    def node_label(self, node):
        parts = [
            "{0.name}",
            "calls: {0.calls.value:n}",
            "time: {0.time.value:f}s",
        ]

        if self.processor.config.memory:
            parts += [
                "memory in: {0.memory_in.value_human_bibyte}",
                "memory out: {0.memory_out.value_human_bibyte}",
            ]

        return r"\n".join(parts).format(node)

    @staticmethod
    def edge_label(edge):
        return edge.calls.value

    def sanity_check(self):
        """Basic checks for certain libraries or external applications.  Raise
        or warn if there is a problem.
        """
        pass

    @abstractmethod
    def add_arguments(self, subparsers, parent_parser, usage):
        pass

    def reset(self):
        pass

    def set_processor(self, processor):
        self.processor = processor

    def start(self):
        """Initialise variables after initial configuration."""
        pass

    def update(self):
        """Called periodically during a trace, but only when should_update is
        set to True.
        """
        raise NotImplementedError("update")

    def should_update(self):
        """Return True if the update method should be called periodically."""
        return False

    def done(self):
        """Called when the trace is complete and ready to be saved."""
        raise NotImplementedError("done")

    @staticmethod
    def ensure_binary(cmd):
        if find_executable(cmd):
            return

        raise PyCallGraphException(
            f'The command "{cmd}" is required to be in your path.'
        )

    @staticmethod
    def normalize_path(path):
        regex_user_expand = re.compile("\A~")  # noqa
        if regex_user_expand.match(path):
            path = os.path.expanduser(path)
        else:
            path = os.path.expandvars(path)  # expand, just in case
        return path

    def prepare_output_file(self):
        if self.fp is None:
            self.output_file = self.normalize_path(self.output_file)
            self.fp = open(self.output_file, "wb")

    def verbose(self, text):
        self.processor.config.log_verbose(text)

    def debug(self, text):
        self.processor.config.log_debug(text)

    @classmethod
    def add_output_file(cls, subparser, defaults, help_msg):
        subparser.add_argument(
            "-o",
            "--output-file",
            type=str,
            default=defaults.output_file,
            help=help_msg,
        )
