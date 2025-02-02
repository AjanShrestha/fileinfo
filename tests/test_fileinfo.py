#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_fileinfo
----------------------------------

Tests for `fileinfo` module.
"""

import pytest
from unittest.mock import patch


from fileinfo.fileinfo import FileInfo


def test_init():
    filename = 'somefile.ext'
    fi = FileInfo(filename)
    assert fi.filename == filename


def test_init_relative():
    filename = "somefile.ext"
    relative_path = f"../{filename}"
    fi = FileInfo(relative_path)
    assert fi.filename == filename


@patch('os.path.getsize')
@patch('os.path.abspath')
def test_get_info(abspath_mock, getsize_mock):
    filename = "somefile.ext"
    original_path = f"../{filename}"

    test_abspath = "some/abs/path"
    abspath_mock.return_value = test_abspath

    test_size = 1234
    getsize_mock.return_value = test_size

    fi = FileInfo(original_path)
    info = fi.get_info()

    abspath_mock.assert_called_with(original_path)
    getsize_mock.assert_called_with(original_path)
    assert fi.get_info() == (filename, original_path, test_abspath, test_size)
