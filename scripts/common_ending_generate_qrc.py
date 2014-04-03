#!/usr/bin/env python
# Copyright (C) 2014 Igor Kushnir <igorkuo AT Google mail>
# License: GPL v3+ (http://www.gnu.org/copyleft/gpl.html)
# common-ending-generate-qrc.py: end of script for creating qrc file for icons.

import os

def end_generating_qrc(path_to_theme, filename, prefix, images, script_name):
    index_file = os.path.join(path_to_theme, "index.theme")

    header = """\
<!DOCTYPE RCC>
<!-- This file was auto-generated by %s -->
<RCC version="1.0">
    <qresource prefix="%s">
        <file>%s</file>
""" % (script_name, prefix, index_file)

    trailer = """\
    </qresource>
</RCC>
"""

    with open(filename, "w") as f:
        f.write(header)
        for img in images:
            f.write("        <file>%s</file>\n" % img)
        f.write(trailer)
