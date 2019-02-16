#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import click
import exiftool
import pathlib
import pprint

# GOAL: iterate through all photos, find exif fields that are truly unique (which may or may not exist across all photos), get the names of those fields, combine that for primary_key - then with a dry run see if that presents any conflicts (eg. where there is still a duplicate detected despite combining unique fields together) - sound right?

# time ./media_organizer.py --scan all/ > output.txt


def get_exif(file):
    with exiftool.ExifTool() as et:
        try:
            return et.get_metadata(file)
        except Exception as e:
            print(f"Error reading exif with file: {file} {e}")


@click.command()
@click.option("--debug", help="Enable debug options", is_flag=True)
@click.option("--scan", help="Files to scan", required=True)
def scan(scan, debug):
    files = list(pathlib.Path(scan).glob("**/[!.]*"))
    unique_exif = {}
    common_exif = set()
    c = 0
    total = len(files)

    for file in files:
        c += 1
        if file.is_dir():
            continue

        print(f"{c}/{total}: Running check on {file}")

        exif = get_exif(str(file))
        if exif is None:
            continue

        pprint.pprint(exif)

        for k, v in exif.items():
            if v in unique_exif.get(k, set()):
                # Key is not unique across files
                print(f"Deleting key {k}: Not unique")
                del unique_exif[k]
                common_exif.append(k)
                continue
            elif k not in common_exif:
                unique_exif.setdefault(k, set()).add(v)

    pprint.pprint(unique_exif)
    print(unique_exif.keys())


if __name__ == "__main__":
    scan()
