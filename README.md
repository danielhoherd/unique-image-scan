[![Build Status](https://travis-ci.com/danielhoherd/unique-image-scan.svg?branch=master)](https://travis-ci.com/danielhoherd/unique-image-scan)

# Unique Image Scan

Scans the given paths for images and identify unique images.

# Long description

Iterate through all photos, find exif fields that are truly unique (which may or may not exist across all photos), get the names of those fields, combine that for primary_key - then with a dry run see if that presents any conflicts (eg. where there is still a duplicate detected despite combining unique fields together) - sound right?


# Installation

This project attempts to follow poetry 1.x best practices.

Simply run:

    $ poetry install .


# Usage

To use it:

    $ unique-image-scan --help


# Development

    $ git clone git@github.com:danielhoherd/unique-image-scan.git && cd unique-image-scan
    $ poetry install --dev
