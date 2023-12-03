#!/usr/bin/env python

import sys
import re

N = {
    "zero":  0,
    "one":   1,
    "two":   2,
    "three": 3,
    "four":  4,
    "five":  5,
    "six":   6,
    "seven": 7,
    "eight": 8,
    "nine":  9
}

def get_num(line):
    m_l = re.search(r"(zero|one|two|three|four|five|six|seven|eight|nine|\d)", line.strip())
    m_r = re.search(r"(orez|eno|owt|eerht|ruof|evif|xis|neves|thgie|enin|\d)", line.strip()[::-1])

    n = 0
    try:
        n = int(N[m_l.group(1)]) * 10
    except:
        n = int(m_l.group(1)) * 10

    try:
        n = n + int(N[m_r.group(1)[::-1]])
    except:
        n = n + int(m_r.group(1)[::-1])

    return n

def main():
    with open("day01.in.utf8", 'r') as FILE:
        print(f"{sum(map(get_num, FILE.readlines()))}")
        FILE.close()

if __name__ == "__main__":
    main()
