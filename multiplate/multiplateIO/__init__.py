# Copyright 2015 Richard Campen
# All rights reserved
# This software is released under the Modified BSD license
# See LICENSE.txt for the full license documentation

"""multiplate 0.1a1
================

Module containing scripts for parsing output files from multiplate readers.

For complete documentation see README.rst.
"""

from . import EnSpireIO

_FormatToParser = {"enspire": EnSpireIO.parse_csv}

def parse_csv(file, format):
    """Parse csv files."""
    with open(file, "r") as in_handle:

        if format in _FormatToParser:
            parser = _FormatToParser[format]
            data = parser(in_handle)

    return data