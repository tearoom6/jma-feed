# Overview

Python client library for JMA feed.

This project was generated with [cookiecutter](https://github.com/audreyr/cookiecutter) using [jacebrowning/template-python](https://github.com/jacebrowning/template-python).

[![Unix Build Status](https://img.shields.io/travis/tearoom6/jma-feed/master.svg?label=unix)](https://travis-ci.org/tearoom6/jma-feed)
[![Coverage Status](https://img.shields.io/coveralls/tearoom6/jma-feed/master.svg)](https://coveralls.io/r/tearoom6/jma-feed)
[![Scrutinizer Code Quality](https://img.shields.io/scrutinizer/g/tearoom6/jma-feed.svg)](https://scrutinizer-ci.com/g/tearoom6/jma-feed/?branch=master)
[![PyPI Version](https://img.shields.io/pypi/v/jma-feed.svg)](https://pypi.org/project/jma-feed)
[![PyPI License](https://img.shields.io/pypi/l/jma-feed.svg)](https://pypi.org/project/jma-feed)

# Setup

## Requirements

* Python 3.7+

## Installation

Install jma-feed with pip:

```sh
$ pip install jma-feed
```

or directly from the source code:

```sh
$ git clone https://github.com/tearoom6/jma-feed.git
$ cd jma-feed
$ python setup.py install
```

# Usage

After installation, the package can imported:

```sh
$ python
>>> import jma_feed
>>> jma_feed.__version__
```

## Low-level API

Fetching feeds:

```python
from jma_feed.feed import AtomFeed

# High-frequency feed
# Regular (定時: 気象に関する情報のうち、天気概況など定時に発表されるもの)
feed_url = 'http://www.data.jma.go.jp/developer/xml/feed/regular.xml'
# Extra (随時: 気象に関する情報のうち、警報・注意報など随時発表されるもの)
feed_url = 'http://www.data.jma.go.jp/developer/xml/feed/extra.xml'
# Earthquake/Volcano (地震火山: 地震、火山に関する情報)
feed_url = 'http://www.data.jma.go.jp/developer/xml/feed/eqvol.xml'
# Others (その他: 上記３種類のいずれにも属さないもの)
feed_url = 'http://www.data.jma.go.jp/developer/xml/feed/other.xml'

# Long-term feed
# Regular (定時: 気象に関する情報のうち、天気概況など定時に発表されるもの)
feed_url = 'http://www.data.jma.go.jp/developer/xml/feed/regular_l.xml'
# Extra (随時: 気象に関する情報のうち、警報・注意報など随時発表されるもの)
feed_url = 'http://www.data.jma.go.jp/developer/xml/feed/extra_l.xml'
# Earthquake/Volcano (地震火山: 地震、火山に関する情報)
feed_url = 'http://www.data.jma.go.jp/developer/xml/feed/eqvol_l.xml'
# Others (その他: 上記３種類のいずれにも属さないもの)
feed_url = 'http://www.data.jma.go.jp/developer/xml/feed/other_l.xml'

feed = AtomFeed(feed_url)

print(feed.id)
print(feed.title)
print(feed.subtitle)
print(feed.updated)
print(feed.rights)
entries = feed.entries
for entry in entries:
    print(entry.id)
    print(entry.title)
    print(entry.updated)
    print(entry.author)
    print(entry.content)
    print(entry.link)
```

