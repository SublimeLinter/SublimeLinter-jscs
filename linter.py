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

from SublimeLinter.lint import Linter, util


class Jscs(Linter):

    """Provides an interface to jscs."""

    syntax = ('javascript', 'html')
    cmd = 'jscs -r inlinesingle'
    version_args = '--version'
    version_re = r'(?P<version>\d+\.\d+\.\d+)'
    version_requirement = '>= 1.4.0'  # 1.4.0 introduced inlinesingle reporter
    regex = r'''(?xi)
        ^.+:\s* # filename
        (?:line.(?P<line>\d+),.col.(?P<col>\d+),.)
        (?P<message>.*)
    '''
    error_stream = util.STREAM_STDOUT
    selectors = {'html': 'source.js.embedded.html'}
    tempfile_suffix = 'js'
    config_file = ('--config', '.jscsrc', '~')
