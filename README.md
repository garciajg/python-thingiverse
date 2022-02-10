# Python Thingiverse

NOT OFFICIAL. This is only a Python wrapper for Thingiverse REST API.


## Building

```bash
python3 -m build
```

## Uploading

```bash
python3 -m twine upload --repository testpypi dist/*
```

## Installing development package

```bash
python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps example-package-YOUR-USERNAME-HERE
```


## TODO:

- [ ] Docstrings
- [ ] OAuth working
- [ ] CI/CD
- [ ] Tests
- [ ] README
- [ ] Think of documentation hosting
