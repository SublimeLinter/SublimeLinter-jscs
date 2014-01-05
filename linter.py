#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Ilya Akhmadullin
# Copyright (c) 2013 Ilya Akhmadullin
#
# License: MIT
#

"""This module exports the jscs plugin class."""

from SublimeLinter.lint import Linter


class Jscs(Linter):

    """Provides an interface to jscs."""

    syntax = ('javascript', 'html', 'html 5')
    cmd = 'jscs -r checkstyle'
    config_file = ('-c', '.jscs.json')
    regex = (
        r'^\s+?<error line="(?P<line>\d+)" '
        r'column="(?P<col>\d+)" '
        # jscs always reports with error severity; show as warning
        r'severity="(?P<warning>error)" '
        r'message="(?P<message>.+?)"'
    )
    multiline = True
    selectors = {'html': 'source.js.embedded.html'}
    tempfile_suffix = 'js'
