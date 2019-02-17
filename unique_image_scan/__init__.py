# -*- coding: utf-8 -*-
import exiftool
import pathlib
import pprint
import progressbar

import sys

assert sys.version_info >= (3, 7, 0), "Python 3.7+ is required."


def debug(text):
    if debug is True:
        print("DEBUG: " + "-" * 60)
        pprint.pprint(text)


def get_exif(file):
    with exiftool.ExifTool() as et:
        try:
            return et.get_metadata(file)
        except Exception as e:
            print(f"Error reading exif with file: {file} {e}")


def scan_source_paths(source_paths):
    files = []
    for path in source_paths:
        files += list(pathlib.Path(path).glob("**/[!.]*"))
    unique_exif = {}
    common_exif = []
    index = 0
    total = len(files)

    progress = progressbar.ProgressBar(max_value=total)

    for file in files:
        index += 1
        progress.update(index)

        if file.is_dir():
            continue

        print(file)

        exif = get_exif(str(file))
        if exif is None:
            continue

        debug(exif)

        for key, value in exif.items():
            if value in unique_exif.get(key, []):
                # Key is not unique across files
                print(f"Deleting key {key}: Not unique")
                del unique_exif[key]
                common_exif.append(key)
                continue
            elif key not in common_exif:
                unique_exif.setdefault(key, []).append(value)

    progress.finish()

    debug(unique_exif)
    print("Final Summary of keys with unique values: " + "-" * 80)
    for key in unique_exif.keys():
        print(key)
