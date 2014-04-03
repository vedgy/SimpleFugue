#!/usr/bin/env python
# Copyright (C) 2008 Patrick Niklaus <marex AT compiz-fusion DOT(.) org>
# Copyright (C) 2014 Igor Kushnir <igorkuo AT Google mail>
# License: GPL v3+ (http://www.gnu.org/copyleft/gpl.html)
# generate-theme.py: creates SimpleFugue index.theme for icons available in
# subdirectories of current directory.

import os

def is_normal(name):
    return name[0] != '.' and name != "__pycache__"

dirs = []

for name in os.listdir("./"):
    if is_normal(name) and name != "scripts" and os.path.isdir(name):
        context_list = os.listdir(name)
        for context in context_list:
            if is_normal(context):
                path = os.path.join(name, context)
                if os.path.isdir(path):
                    dirs.append(path)

name = "SimpleFugue"
comment = "SimpleFugue theme based on Tango"
inherits = "tango,hicolor"
example = "help-about"
dirlist = ",".join(dirs)

header = """\
[Icon Theme]
Name=%s
Comments=%s
Inherits=%s

Example=%s

Directories=%s

"""
header = header % (name, comment, inherits, example, dirlist)

context_table = {
    'apps': "Applications",
    'actions': "Actions",
    'categories': "Categories",
    'devices': "Devices",
    'mimetypes': "MimeTypes",
    'places': "Places",
    'status': "Status",
    'animations': "Animations"
}

fixed_sizes = ("8x8", "16x16", "22x22", "24x24", "32x32", "48x48", "96x96",
               "256x256")
scalable_sizes = ("scalable")

with open("index.theme", "w") as f:
    f.write(header)
    for dir in dirs:
        size, context = dir.split(os.sep)
        f.write("[%s]\n" % dir)
        if size in scalable_sizes:
            f.write("Size=128\n")
            f.write("Type=Scalable\nMinSize=1\nMaxSize=1024\n")
        elif size in fixed_sizes:
            f.write("Size=%s\n" % size.split("x")[0])
            f.write("Type=Fixed\n")
        else:
            sys.exit('ERROR: unknown size "', size, '".')
        f.write("Context=%s\n" % context_table[context])
        f.write('\n')
