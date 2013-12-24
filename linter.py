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

    syntax = ('javascript')
    executable = 'jscs'
    cmd = 'jscs -r checkstyle'
    regex = (
        r'.+?\<error line=\"(?P<line>\d+)\" '
        r'column=\"(?P<col>\d+)\" '
        # jscs always reports with error severity; show as warning
        r'severity=\"(?P<warning>error)\" '
        r'message=\"(?P<message>.+)\" source'
    )
    multiline = True
    # currently jscs does not accept stdin so this does not work
    # selectors = {'html': 'source.js.embedded.html'}
    tempfile_suffix = 'js'
