#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_fileinfo
----------------------------------

Tests for `fileinfo` module.
"""

import pytest


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
