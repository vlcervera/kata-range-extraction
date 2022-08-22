# Template for python/poetry projects

This is a template to get a boilerplate structure to start to develop with Python.

## Python version

This template uses Python 3.9. You can use pyenv to configure your environment.

```
https://github.com/pyenv/pyenv#installation
```

## Install
You can install all dependencies required for this project using:
````shell
make install
````

## Linter
You can apply linter and format tools using:
````shell
make lint
````

## Format
You can apply format tools isolated from linter in case of linter fails using:
````shell
make format
````

## Test
You can run the test suite using:
````shell
make test
````