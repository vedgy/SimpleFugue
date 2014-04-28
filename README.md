## Introduction

<b>SimpleFugue</b> is an icon theme based on Tango theme. It contains only
limited number of icons and should be used along with Tango theme. It can also
be used to provide applications with default icons.

The Tango base icon theme (public domain) can be downloaded at
http://tango.freedesktop.org/releases/tango-icon-theme-0.8.90.tar.gz

This repository is not ready to use because of missing png icons. One of Bash
shell scripts can be used to get complete theme:
* `download_all_png` script downloads generated icons (requires wget or curl);
* `generate_all_png` generates png icons locally from svg (requires inkscape).

If both `README_generated` and `README.md` files are present in the root
`SimpleFugue` directory, then this version of theme is (most likely)
complemented with some or all generated png icons.

Apart from icons, SimpleFugue theme contains several convenience scripts:
* `download_all_png` (Bash shell script) - downloads auto-generated icons.
* `generate_theme.py` (Python script) - creates index.theme, which references
all icons available in `SimpleFugue` subdirectories.

In `scripts` subdirectory:
* `generate_png`, `generate_png_small`, `generate_png_apps_big`,
`generate_specified_png` (Bash shell scripts) -
create png icons out of scalable icons using inkscape.
* `common_ending_generate_qrc.py`, `generate_qrc.py`, `generate_qrc_2.py`
(Python scripts) - create qrc file with index.theme and specified icons.

## License

Copyright (C) 2014 Igor Kushnir <igorkuo AT Google mail>

SimpleFugue is licensed under the <b>GNU GPLv3+</b> license,
a copy of which can be found in the `COPYING` file.

SimpleFugue is free software: you can redistribute it and/or
modify it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

SimpleFugue is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with
SimpleFugue.  If not, see <http://www.gnu.org/licenses/>.
