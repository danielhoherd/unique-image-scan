# -*- coding: utf-8 -*-
import exiftool
import hashlib
import pathlib
import pprint
import progressbar

import sys

from unique_image_scan import models

assert sys.version_info >= (3, 7, 0), "Python 3.7+ is required."

BUF_SIZE = 65536

def file_hash(file):
    if not file:
        return

    sha256 = hashlib.sha256()

    with open(file, 'rb') as f:
        while True:
            data = f.read(BUF_SIZE)
            if not data:
                break
            sha256.update(data)

    return sha256.hexdigest()

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
    results = []
    for path in source_paths:
        results += list(pathlib.Path(path).glob("**/[!.]*"))
    files = [f for f in results if f.is_file()]
    unique_exif = {}
    common_exif = []
    index = 0
    total = len(files)
    scanned = {}

    progress = progressbar.ProgressBar(max_value=total)

    for file in files:
        index += 1
        progress.update(index)

        if file.is_dir():
            continue

        print(file)
        scanned_key_check = (file.name, file.stat().st_size)
        if scanned_key_check in scanned:
            # We may have already scanned this file, let's see
            previous_file_hash = file_hash(scanned[scanned_key_check])
            current_file_hash = file_hash(str(file))
            if previous_file_hash == current_file_hash:
                # Let's be extra sure it's the same file
                print(f'... Skipping, already scanned')
                continue
        scanned[(file.name, file.stat().st_size)] = str(file)

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
    uniq_count = len(unique_exif)
    print(f"Final Summary of {uniq_count} keys with unique values: " + "-" * 80)
    session = models.create_session()
    for key in unique_exif.keys():
        print(key)
        new_key = models.UniqueKey(name=key)
        session.add(new_key)
    session.commit()
    session.close()
