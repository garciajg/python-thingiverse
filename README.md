# Python Thingiverse

NOT OFFICIAL. This is only a Python wrapper for Thingiverse REST API.

This project was started in Feb 10 2022. It is still being developed and improved. To see the Test PyPI package, check it [here](https://test.pypi.org/project/python-thingiverse/)

Check out full (documentation)[https://garciajg.github.io/python-thingiverse/]

## Table of Contents

+ [Getting Started](#getting-started)
  + [Usage](#usage)
+ [Installing development package](#installing-development-package)
+ [TODO](#todo)
+ [Improvements](#improvements)


### Getting Started

To install the package run

```bash
pip install python-thingiverse
```


#### Usage

Initializing the Thingiverse

```python
from thingiverse import Thingiverse

thingy = Thingiverse(access_token="<access token>")
search_results = thingy.search_term("RPi 4")
```


### Installing development package

```bash
python3 -m pip install -i https://test.pypi.org/simple/ python-thingiverse
```


### TODO:

- A full list of REST endpoints will go here

### Improvements

- [X] Docstrings
- [X] OAuth working (Use App token!!!)
- [X] CI/CD
- [ ] Look into autoversioning
- [X] Tests (started)
- [X] README (in progress)
- [X] Think of documentation hosting
