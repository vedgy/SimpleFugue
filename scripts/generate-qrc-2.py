#!/usr/bin/env python
# Copyright (C) 2014 Igor Kushnir <igorkuo AT Google mail>
# License: GPL v3+ (http://www.gnu.org/copyleft/gpl.html)
# generate-qrc-2.py: creates qrc file for the list of icons from file that is
# specified as a command line argument.

import os, sys
from collections import defaultdict

if len(sys.argv) < 4:
    sys.exit("""\
Not enough arguments!
First argument must be a relative path to theme directory.
Second argument must be a resulting filename.
Third argument must be a filename of file that contains list of icons.
""")

def is_normal(name):
    return name[0] != '.'

path_to_theme = sys.argv[1]
filename = sys.argv[2]
icon_list_filename = sys.argv[3]

icon_dict = defaultdict(list)
with open(icon_list_filename, "r") as f:
    for line in f:
        dir_and_file = os.path.split(line.rstrip('\n'))
        if dir_and_file[0] and dir_and_file[1]:
            icon_dict[dir_and_file[0]].append(dir_and_file[1])
images = []

def is_valid_icon(f, l):
    return (f[-1] != '~') and (os.path.splitext(f)[0] in l)

dir_list0 = os.listdir(path_to_theme)
for d0 in dir_list0:
    path0 = os.path.join(path_to_theme, d0)
    if os.path.isdir(path0):
        dir_list1 = os.listdir(path0)
        for d1 in dir_list1:
            path1 = os.path.join(path0, d1)
            if os.path.isdir(path1):
                names = icon_dict.get(d1)
                if names != None:
                    file_list = os.listdir(path1)
                    for f in file_list:
                        path2 = os.path.join(path1, f)
                        if os.path.isfile(path2) and is_valid_icon(f, names):
                            images.append(path2)

script_name = "generate-qrc-2.py"

from common_ending_generate_qrc import end_generating_qrc
end_generating_qrc(path_to_theme, filename, images, script_name)
