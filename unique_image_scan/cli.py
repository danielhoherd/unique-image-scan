#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import click

import unique_image_scan


@click.group()
def main():
    """
    Iterate through all photos, find exif fields that are truly unique
    (which may or may not exist across all photos), get the names of
    those fields, combine that for primary_key - then with a dry run
    see if that presents any conflicts (eg. where there is still a
    duplicate detected despite combining unique fields together) -
    sound right?
    """


@main.command()
@click.argument("source_paths", nargs=-1, required=True)
def scan(source_paths):
    """
    Scans the given paths for source images. Individual files are not allowed.
    """

    unique_image_scan.scan_source_paths(source_paths)


if __name__ == "__main__":
    main()
