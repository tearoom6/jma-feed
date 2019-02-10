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

```python
import jma_feed
jma_feed.__version__
```

Report can be retrieved from Atom feeds:

```python
all_reports = jma_feed.fetch_all_reports(long_term=False)
all_meteorology_reports = jma_feed.fetch_all_meteorology_reports(long_term=False)
all_seismology_reports = jma_feed.fetch_all_seismology_reports(long_term=False)
all_volcanology_reports = jma_feed.fetch_all_volcanology_reports(long_term=False)
```

Report API:

```python
control = report.control
print(control.title)
print(control.date_time)
print(control.status)
print(control.editorial_office)
print(control.publishing_office)

head = report.head
print(head.title)
print(head.report_date_time)
print(head.target_date_time)
print(head.event_id)
print(head.info_type)
print(head.serial)
print(head.info_kind)
print(head.info_kind_version)
print(head.headline_text)
for headline_information in head.headline_information_list:
    print(headline_information.type)
    for item in headline_information.items:
        print(item.areas_code_type)
        for kind in item.kinds:
            print(kind.name)
            print(kind.code)
            print(kind.condition)
        for area in item.areas:
            print(area.name)
            print(area.code)

body = report.body

# Meteorology
if isinstance(body, jma_feed.ReportBodyMeteorology):
    target_area = body.target_area
    if target_area:
        print(target_area.name)
        print(target_area.code)
    comment = body.comment
    if comment:
        for text in comment.texts:
            print(text.text)
    for notice in body.notices:
        print(notice)
    for warning in body.warnings:
        for item in warning.items:
            print(item.change_status)
            print(item.full_status)
            print(item.editing_mark)
            if item.area:
                print(item.area.name)
                print(item.area.code)
            for kind in item.kinds:
                print(kind.name)
                print(kind.code)
                print(kind.status)
                print(kind.condition)
    for meteorological_info in body.meteorological_infos:
        print(meteorological_info.date_time)
        print(meteorological_info.duration)
        print(meteorological_info.name)
        for item in meteorological_info.items:
            print(item.change_status)
            print(item.full_status)
            print(item.editing_mark)
            if item.area:
                print(item.area.name)
                print(item.area.code)
            for kind in item.kinds:
                print(kind.name)
                print(kind.code)
                print(kind.status)
                print(kind.condition)
    for time_series_info in body.time_series_infos:
        for time_define in meteorological_info.time_defines:
            print(time_define.date_time)
            print(time_define.duration)
            print(time_define.name)
        for item in meteorological_info.items:
            print(item.change_status)
            print(item.full_status)
            print(item.editing_mark)
            if item.area:
                print(item.area.name)
                print(item.area.code)
            for kind in item.kinds:
                print(kind.name)
                print(kind.code)
                print(kind.status)
                print(kind.condition)

# Seismology
if isinstance(body, jma_feed.ReportBodySeismology):
    print(body.naming)
    print(body.text)
    print(body.next_advisory)
    comments = body.comments
    if comments and comments.warning_comment:
        print(comments.warning_comment.text)
        print(comments.warning_comment.code)
        print(comments.warning_comment.code_type)
    if comments and comments.forecast_comment:
        print(comments.forecast_comment.text)
        print(comments.forecast_comment.code)
        print(comments.forecast_comment.code_type)
    if comments and comments.observation_comment:
        print(comments.observation_comment.text)
        print(comments.observation_comment.code)
        print(comments.observation_comment.code_type)
    if comments and comments.var_comment:
        print(comments.var_comment.text)
        print(comments.var_comment.code)
        print(comments.var_comment.code_type)
    if comments and comments.free_form_comment:
        print(comments.free_form_comment)
    tsunami = body.tsunami
    for earthquake in body.earthquakes:
        print(earthquake.origin_time)
        print(earthquake.arrival_time)
        print(earthquake.condition)
        for magnitude in earthquake.magnitudes:
            print(magnitude)
        hypocenter = earthquake.hypocenter
        if hypocenter:
            print(hypocenter.source)
            if hypocenter.area:
                print(hypocenter.area.name)
                print(hypocenter.area.code)
                print(hypocenter.area.coordinate)

# Volcanology
if isinstance(body, jma_feed.ReportBodyVolcanology):
    print(body.notice)
    print(body.text)
    for volcano_info in body.volcano_infos:
        for item in volcano_info.items:
            if item.kind:
                print(item.kind.name)
                print(item.kind.formal_name)
                print(item.kind.code)
                print(item.kind.condition)
            for area in item.areas:
                print(area.name)
                print(area.code)
                print(area.coordinate)
    for ash_info in body.ash_infos:
        print(ash_info.start_time)
        print(ash_info.end_time)
        for item in ash_info.items:
            if item.kind:
                print(item.kind.name)
                print(item.kind.formal_name)
                print(item.kind.code)
                print(item.kind.condition)
            for area in item.areas:
                print(area.name)
                print(area.code)
                print(area.coordinate)
```

Feed API (Low-level API):

```python
# High-frequency feed
# Regular (定時: 気象に関する情報のうち、天気概況など定時に発表されるもの)
feed_url = jma_feed.FEED_URL_REGULAR_SHORT_TERM
# Extra (随時: 気象に関する情報のうち、警報・注意報など随時発表されるもの)
feed_url = jma_feed.FEED_URL_EXTRA_SHORT_TERM
# Earthquake/Volcano (地震火山: 地震、火山に関する情報)
feed_url = jma_feed.FEED_URL_EQVOL_SHORT_TERM
# Others (その他: 上記３種類のいずれにも属さないもの)
feed_url = jma_feed.FEED_URL_OTHER_SHORT_TERM

# Long-term feed
# Regular (定時: 気象に関する情報のうち、天気概況など定時に発表されるもの)
feed_url = jma_feed.FEED_URL_REGULAR_LONG_TERM
# Extra (随時: 気象に関する情報のうち、警報・注意報など随時発表されるもの)
feed_url = jma_feed.FEED_URL_EXTRA_LONG_TERM
# Earthquake/Volcano (地震火山: 地震、火山に関する情報)
feed_url = jma_feed.FEED_URL_EQVOL_LONG_TERM
# Others (その他: 上記３種類のいずれにも属さないもの)
feed_url = jma_feed.FEED_URL_OTHER_LONG_TERM

feed = jma_feed.AtomFeed(feed_url)

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

