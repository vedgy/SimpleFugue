#!/usr/bin/env python
# Copyright (C) 2014 Igor Kushnir <igorkuo AT Google mail>
# License: GPL v3+ (http://www.gnu.org/copyleft/gpl.html)
# generate-qrc.py: creates qrc file for icons, which names are specified as
# command line arguments.

import os, sys

if len(sys.argv) < 4:
    sys.exit("""\
Not enough arguments!
First argument must be a relative path to theme directory.
Second argument must be a resulting filename.
Then a nonempty list of icon names, which are to be included in qrc file, must \
follow.
""")

def is_normal(name):
    return name[0] != '.'

path_to_theme = sys.argv[1]
dir_list = os.listdir(path_to_theme)
filename = sys.argv[2]
icon_names = [name for name in sys.argv[3:] if name]

images = []

def is_valid_icon(f):
    return (f[-1] != '~') and (os.path.splitext(f)[0] in icon_names)

for name in dir_list:
    if is_normal(name):
        for path, dirs, files in os.walk(os.path.join(path_to_theme, name)):
            files = [f for f in files if is_valid_icon(f)]
            dirs[:] = [d for d in dirs if is_normal(d)]
            images += [os.path.join(path, f) for f in files]

script_name = "generate-qrc.py"

from common_ending_generate_qrc import end_generating_qrc
end_generating_qrc(path_to_theme, filename, images, script_name)
