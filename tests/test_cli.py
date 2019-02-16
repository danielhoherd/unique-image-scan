# -*- coding: utf-8 -*-
import pytest
from click.testing import CliRunner
import re

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
