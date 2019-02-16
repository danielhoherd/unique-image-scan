# -*- coding: utf-8 -*-
import exiftool
import pathlib
import pprint


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
    for path in source_paths:
        files = list(pathlib.Path(path).glob("**/[!.]*"))
    unique_exif = {}
    common_exif = []
    index = 0
    total = len(files)

    for file in files:
        index += 1
        if file.is_dir():
            continue

        print(f"{index}/{total} {index/total*100:.0f}%: Running check on {file}")

        exif = get_exif(str(file))
        if exif is None:
            continue

        debug(exif)

        for k, v in exif.items():
            if v in unique_exif.get(k, []):
                # Key is not unique across files
                print(f"Deleting key {k}: Not unique")
                del unique_exif[k]
                common_exif.append(k)
                continue
            elif k not in common_exif:
                unique_exif.setdefault(k, []).append(v)

    debug(unique_exif)
    print("Final Summary of keys with unique values: " + "-" * 80)
    for key in unique_exif.keys():
        print(key)
