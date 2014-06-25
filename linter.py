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

    syntax = ('javascript', 'html', 'javascriptnext')
    cmd = 'jscs -r checkstyle'
    version_args = '--version'
    version_re = r'(?P<version>\d+\.\d+\.\d+)'
    version_requirement = '>= 1.0.10'  # 1.0.10 introduced checkstyle reporter
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
    config_file = ('--config', '.jscsrc', '~')
