#!/usr/bin/env python

import sys
import re

def get_num(line):
    print(line.strip().split(": ")[1].split('; '))
    return 0

def main():
    with open("day02.in.utf8", 'r') as FILE:
        with open("day02.out.utf8", 'w') as O_FILE:
            O_FILE.write(f"{sum(map(get_num, FILE.readlines()))}\n")
            O_FILE.close()
        FILE.close()

if __name__ == "__main__":
    main()
