# Installation

![Undraw Installation](../static/img/undraw_Setup_wizard_re_nday.png)

::: danger Python version
Before starting, you should know that PyBase doesn't have support
for Python 2.7, only Python 3.x onwards.
:::

## Using pip
```sh
# Stable version
python3 -m pip install -U pybase_db

# Pre-release (Development) version
python3 -m pip install -U --pre pybase_db

# From github's latest commit
# Available branches:
#   • master (recommended)
#   • development (unstable releases)
python3 -m pip install -U git+https://github.com/PyBase/PyBase@branch
```

::: warning Missing external dependencies
Installing from the last repository commit on GitHub will not install external PyBase dependencies!
:::

## Building
The development branch changes aren't compiled and uploaded to Pypi every time,
so you must compile a wheel yourself to test the experimental stuff if the newest
changes aren't uploaded to Pypi.
```sh
python3 setup.py bdist_wheel

python3 -m pip install -U dist/pybase_db-version-py3-none-any.whl
```
