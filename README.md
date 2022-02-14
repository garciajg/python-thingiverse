# Python Thingiverse

[![Total alerts](https://img.shields.io/lgtm/alerts/g/garciajg/python-thingiverse.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/garciajg/python-thingiverse/alerts/)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/garciajg/python-thingiverse.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/garciajg/python-thingiverse/context:python)


NOT OFFICIAL. This is only a Python wrapper for Thingiverse REST API.

This project was started in Feb 10 2022. It is still being developed and improved. To see the Test PyPI package, check it [here](https://test.pypi.org/project/python-thingiverse/).

This project uses [python-box](https://pypi.org/project/python-box/) enpoint response. Python Box allows for use of dot-notation in dictionaries, this includes making inaccessible keys safe to access as well.

```python
# From python-box documentation https://pypi.org/project/python-box/
from box import Box

movie_box = Box({ "Robin Hood: Men in Tights": { "imdb stars": 6.7, "length": 104 } })

movie_box.Robin_Hood_Men_in_Tights.imdb_stars
# 6.7
```

Check out full (python-thingiverse documentation)[https://garciajg.github.io/python-thingiverse/]

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

- `PATCH /users/{$username}/`
- `DELETE /users/{$username}/`


### Improvements

- [X] Docstrings
- [X] OAuth working (Use App token!!!)
- [X] CI/CD
- [ ] Look into autoversioning
- [X] Tests (started)
- [X] README (in progress)
- [X] Think of documentation hosting
