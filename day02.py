#!/usr/bin/env python

import sys
import re

def get_num(line):
    r_max = 0
    g_max = 0
    b_max = 0
    
    for grab in line.strip().split(": ")[1].split('; '):
        try:
            r_max = max(r_max, int(re.search(r"(\d+) red", grab).group(1)))
        except:
            pass

        try:
            g_max = max(g_max, int(re.search(r"(\d+) green", grab).group(1)))
        except:
            pass
        
        try:
            b_max = max(b_max, int(re.search(r"(\d+) blue", grab).group(1)))
        except:
            pass

    return (r_max * g_max * b_max)

def main():
    with open("day02.in.utf8", 'r') as FILE:
        print(f"{sum(map(get_num, FILE.readlines()))}")
        FILE.close()

if __name__ == "__main__":
    main()
