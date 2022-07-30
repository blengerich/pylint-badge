# pylint-badge

![pylint Score](pylint.svg)

A simple and functional `pylint` badge generator.

This version makes a minor fix of [pylint-badge](https://github.com/rossi-fi/pylint-badge) to support multiple versions of `pylint`.

Better to use [anybadge](https://github.com/jongracecox/anybadge) for most purposes.


## How to Use

1. Install via `pip` or other method:
`pip install git+https://github.com/blengerich/pylint-badge`

2. Run as follows: `pylint-badge script.py pylint.svg` which will produce a file `pylint.svg` in the current directory.

3. Add to your README.md:
`![pylint Score](pylint.svg)`

## Color intervals

By Default:
0.00 < ![pylint Score](https://mperlet.github.io/pybadge/badges/1.50.svg) < 3.00 < ![pylint Score](https://mperlet.github.io/pybadge/badges/5.51.svg) < 7.00 ![pylint Score](https://mperlet.github.io/pybadge/badges/9.73.svg) < 10.00

The thresholds for colors can be changed by the args:
```
--min_yellow
--min_green
```
which set the minimum threshold of `pylint` score for the yellow or green colors to be assigned.

## Limitations

* Negative scores are not supported


## Idea

Forked from [pylint-badge](https://github.com/rossi-fi/pylint-badge), which was "Inspired by mperlet's [pybadge](https://github.com/mperlet/pybadge), which was in turn inspired by [this blogpost](http://www.desmondrivet.com/blog/technical/pylint-badges.html.)"
