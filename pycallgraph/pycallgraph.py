import locale

from .config import Config
from .exceptions import PyCallGraphException
from .output import Output
from .tracer import AsynchronousTracer, SynchronousTracer


class PyCallGraph(object):
    def __init__(self, output=None, config=None):
        """output can be a single Output instance or an iterable with many
        of them.  Example usage:

            PyCallGraph(output=GraphvizOutput(), config=Config())
        """
        locale.setlocale(locale.LC_ALL, "")

        self.tracer = None

        if output is None:
            self.output = []
        elif isinstance(output, Output):
            self.output = [output]
        else:
            self.output = output

        self.config = config or Config()

        configured_ouput = self.config.get_output()
        if configured_ouput:
            self.output.append(configured_ouput)

        self.reset()

    def __enter__(self):
        self.start()

    def __exit__(self, type, value, traceback):
        self.done()

    def get_tracer_class(self):
        if self.config.threaded:
            return AsynchronousTracer
        else:
            return SynchronousTracer

    def reset(self):
        """Resets all collected statistics.  This is run automatically by
        start(reset=True) and when the class is initialized.
        """
        self.tracer = self.get_tracer_class()(self.output, config=self.config)

        for output in self.output:
            self.prepare_output(output)

    def start(self, reset=True):
        """Begins a trace.  Setting reset to True will reset all previously
        recorded trace data.
        """
        if not self.output:
            raise PyCallGraphException(
                "No outputs declared. Please see the "
                "examples in the online documentation."
            )

        if reset:
            self.reset()

        for output in self.output:
            output.start()

        self.tracer.start()

    def stop(self):
        """Stops the currently running trace, if any."""
        self.tracer.stop()

    def done(self):
        """Stops the trace and tells the outputters to generate their
        output.
        """
        self.stop()

        self.generate()

    def generate(self):
        # If in threaded mode, wait for the processor thread to complete
        self.tracer.done()

        for output in self.output:
            output.done()

    def add_output(self, output):
        self.output.append(output)
        self.prepare_output(output)

    def prepare_output(self, output):
        output.sanity_check()
        output.set_processor(self.tracer.processor)
        output.reset()

def main():
    import os, sys
    # Inject the current working directory so modules can be imported.
    sys.path.insert(0, os.getcwd())

    import pycallgraph as __pycallgraph

    __config = __pycallgraph.Config()
    __config.parse_args()
    __config.strip_argv()

    globals()['__file__'] = __config.command

    __file_content = open(__config.command).read()

    with __pycallgraph.PyCallGraph(config=__config):
        exec(__file_content)

if __name__ == '__main__':
    main()
