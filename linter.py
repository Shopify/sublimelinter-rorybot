#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Sindre Sorhus
# Copyright (c) 2015 Sindre Sorhus
#
# License: MIT
#

from SublimeLinter.lint import NodeLinter


class Rorybot(NodeLinter):
    cmd = 'rorybot'
    regex = r'^\s+(?P<line>\d+):(?P<col>\d+).+(?:(?P<warning>warning)) (?P<message>.+)'
    selectors = {
        'html': 'text.html.basic'
    }
    syntax = (
        'markdown',
        'markdown extended',
        'multimarkdown',
        'plain text',
        'ruby',
        'html (rails)',
        'html'
    )
    version_args = '--version'
    version_re = r'(?P<version>\d+\.\d+\.\d+)'
    version_requirement = '>=0.0.0'
