# CallGraph4Py

![](https://img.shields.io/badge/Project%20Status-Under%20Development-green)

[![PyPI version](https://badge.fury.io/py/callgraph4py.svg)](https://badge.fury.io/py/callgraph4py)
![Build and Test](https://github.com/e-alizadeh/pycallgraph/workflows/Build%20and%20Test/badge.svg?branch=master)
![MIT License](https://img.shields.io/badge/License-MIT-blueviolet)
[![Code Style: Black](https://img.shields.io/badge/Code%20style-black-black)](https://github.com/psf/black)

---
[![SonarCloud](https://sonarcloud.io/images/project_badges/sonarcloud-white.svg)](https://sonarcloud.io/dashboard?id=e-alizadeh_pycallgraph)

[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=e-alizadeh_pycallgraph&metric=coverage)](https://sonarcloud.io/dashboard?id=e-alizadeh_pycallgraph)
[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=e-alizadeh_pycallgraph&metric=security_rating)](https://sonarcloud.io/dashboard?id=e-alizadeh_pycallgraph)
[![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=e-alizadeh_pycallgraph&metric=vulnerabilities)](https://sonarcloud.io/dashboard?id=e-alizadeh_pycallgraph)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=e-alizadeh_pycallgraph&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=e-alizadeh_pycallgraph)
[![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=e-alizadeh_pycallgraph&metric=reliability_rating)](https://sonarcloud.io/dashboard?id=e-alizadeh_pycallgraph)
[![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=e-alizadeh_pycallgraph&metric=ncloc)](https://sonarcloud.io/dashboard?id=e-alizadeh_pycallgraph)
---

NOTE
---
This is a maintained fork of the excellent [PyCallGraph](https://github.com/gak/pycallgraph) project.
The latest version is **1.0.1**, and was released on 2013-09-17. 
The next release starts from **2.0.0** due to deprecating Python 2.  

Quick Start
-----------
Installation is easy as:

    pip install callgraph4py


Python Call Graph
-----------------
Welcome! Python Call Graph is a [Python](http://www.python.org) module
that creates [call graph](http://en.wikipedia.org/wiki/Call_graph)
visualizations for Python applications.

Screenshots
-----------
Click on the images below to see a larger version and the source code
that generated them.

![image](https://pycallgraph.readthedocs.io/en/develop/_images/basic_thumb.png)
![image](https://pycallgraph.readthedocs.io/en/develop/_images/regexp_grouped_thumb.png)
![image](https://pycallgraph.readthedocs.io/en/develop/_images/regexp_ungrouped_thumb.png)

Features
--------
-   Support for Python 3.7+.
-   Static visualizations of the call graph using Graphviz.
-   Execute pycallgraph from the command line or import it in your code.
-   Customisable colors. You can programatically set the colors based on
    number of calls, time taken, memory usage, etc.
-   Modules can be visually grouped together.
-   Easily extendable to create your own output formats.

Command-line interface
----------------------

The following commands shall collect the call graph into the specified output file in .dot format, which can then be visualized as an SVG image:

```
pycallgraph graphviz --output-format=dot --output-file=script.dot -- ./script.py
dot -Tsvg script.dot > script.svg
```

Development
-----------

Clone this repository and issue a `poetry install` command, in order to install the current version of package.
