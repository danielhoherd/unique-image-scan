# -*- coding: utf-8 -*-
import pytest
from click.testing import CliRunner
import re
import requests
import tempfile
import os


from unique_image_scan import cli


@pytest.fixture
def runner():
    return CliRunner()


def test_cli(runner):
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    assert not result.exception
    assert re.search(r"Iterate through all photos", result.output)


def test_cli_with_arg(runner):
    result = runner.invoke(cli.main, ["scan"])
    assert result.exception
    assert result.exit_code == 2
    assert re.search(r"Error: Missing argument", result.output)


def test_all_images(runner):
    with open("tests/test_urls.txt", "r") as images:
        for image in images:
            image.rstrip()
            tempdir = tempfile.mkdtemp()
            r = requests.get(image, allow_redirects=True)
            open(f"{tempdir}/{os.path.basename(image)}", "wb").write(r.content)
            result = runner.invoke(cli.main, ["scan", tempdir])
            assert not result.exception
