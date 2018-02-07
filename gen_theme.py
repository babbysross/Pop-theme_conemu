# -*- coding: utf-8 -*-
"""
    gen_theme
    ~~~~~~~~~

    ConEmu theme generator

    :copyright: (c) 2015 - present by Radmon.
"""

import re

# **pop color scheme**

palette = [
'#362d29',     # Brown
'#b267e6',     # Purple
'#ffc977',     # Tan
'#8bced6',     # LightBlue
'#cd9731',     # Gold
'#73c48f',     # LightGreen
'#05a6b3',     # BLue
'#bebebe',     # LightGray
'#ffcb6b',     # LightOrange
'#faa41a',     # Orange
'#73c48f',     # LightGreen
'#89ddff',     # LightBlue
'#f44747',     # Red
'#b2ccd6',     # Blue/Gray
'#73c48f',     # LightGreen
'#f44747',     # Red

# **default extended colors**
# I leave it unchanged.
'#000000', # Black
'#000080', # DarkBlue
'#008000', # DarkGreen
'#008080', # DarkCyan
'#800000', # DarkRed
'#800080', # DarkMagenta
'#808000', # DarkYellow
'#c0c0c0', # Gray
'#808080', # DarkGray
'#0000ff', # Blue
'#00ff00', # Green
'#00ffff', # Cyan
'#ff0000', # Red
'#ff00ff', # Magenta
'#ffff00', # Yellow
'#ffffff', # White
]

line = '<value name="ColorTable{0:02}" type="dword" data="00{3}{2}{1}"/>'


def get_rgb(color):
    m = re.match(r'#([0-9a-fA-F]{2})([0-9a-fA-F]{2})([0-9a-fA-F]{2})', color)
    if m is None:
        raise RuntimeError('Invalid color format: %s, #rrggbb expected' % color)
    else:
        return m.groups()


def gen_theme():
    for i in range(0, len(palette)):
        color = palette[i]
        r, g, b = map(lambda x: x.lower(), get_rgb(color))
        yield line.format(i, r, g, b)


if __name__ == '__main__':
    out = '\n'.join(gen_theme())
    print(out)
