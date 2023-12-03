#!/usr/bin/env python

import sys
import re
import numpy as np

def pad_dots(schematic):
    padded_tb = np.concatenate([ np.array([ b'.' * len(schematic[0]) ]), schematic, np.array([ b'.' * len(schematic[0]) ]) ])
    padlr = np.vectorize(lambda x: b'.' + x + b'.')
    padded = padlr(padded_tb)
    return padded

def main():
    p_schem = pad_dots( np.loadtxt("./day03.in.utf8", dtype=bytes, comments=None) )
    pat_num = re.compile(r"\d+")
    pat_dots = re.compile(r"^\.+$")

    s=0

    for (k, v) in enumerate(p_schem):
        for m in pat_num.finditer(v.decode()):
            top = p_schem[k-1][m.start()-1:m.start() + len(m.group()) + 1]
            mid = p_schem[ k ][m.start()-1:m.start() + len(m.group()) + 1]
            bot = p_schem[k+1][m.start()-1:m.start() + len(m.group()) + 1]
            checkstr = top + mid[:1] + mid[-1:] + bot
            
            if not pat_dots.search(checkstr.decode()):
                s = s + int(m.group())

    print(f"{s}")

if __name__ == "__main__":
    main()
