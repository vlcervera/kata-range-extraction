# Range extraction

A format for expressing an **ordered list of integers** is to use a **comma separated** list of either:
- **Individual** integers.
- A **range of integers** denoted by the starting integer separated from the end integer in the range by a dash, '-'.

The range includes all integers in the interval including both endpoints. 

**It is not considered a range unless it spans at least 3 numbers**, for example "12,13,15-17".

Complete the solution so that it takes a list of integers in increasing order and returns a correctly formatted string in the range format.

Example:
Given: [-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]
Output is "-6,-3-1,3-5,7-11,14,15,17-20"

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
