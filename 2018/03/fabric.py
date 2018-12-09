# solution to Advent of Code 2018, day 3 part one and two
# https://adventofcode.com/2018/day/3
#
# Usage: fabric.py [inputfile]

import fileinput
import re
from collections import defaultdict

def main():
    claims = list(parse_claim(line) for line in fileinput.input())

    fabric = defaultdict(dict)

    for claim in claims:
        for y in range(claim['start_y'], claim['start_y'] + claim['dim_y']):
            for x in range(claim['start_x'], claim['start_x'] + claim['dim_x']):
                if x not in fabric[y]:
                    fabric[y][x] = 0
                fabric[y][x] += 1

    # solve part one
    overlap_area = sum(1 for row in fabric.keys() for v in fabric[row].values() if v > 1)
    print(f"Sq. inches with multiple claims: {overlap_area}")

    # solve part two
    for claim in claims:
        if not has_overlap(claim, fabric):
            print(f"Claim with no overlaps: {claim['id']}")
            return


# parse_claim()
#
# Input:
#   instr - claim string, for example "#1 @ 1,3: 4x4"
#
# Returns a dict containing values extracted from input
#   'id', 'start_x', 'start_y', 'dim_x', 'dim_y'
#
def parse_claim(instr):
    match = re.search('#(\d+).+?(\d+),(\d+):.+?(\d+)x(\d+)', instr)
    if match:
        claim = {}
        claim['id'] = match.group(1)
        claim['start_x'] = int(match.group(2))
        claim['start_y'] = int(match.group(3))
        claim['dim_x'] = int(match.group(4))
        claim['dim_y'] = int(match.group(5))
    return claim


# has_overlap()
#
# Input:
#   claim - a claim dict (see parse_claim())
#   fabric - dict-of-dicts with calculated overlaps
#
# Returns True if the claim overlaps with another claim,
#   False if not
#
def has_overlap(claim, fabric):
    for y in range(claim['start_y'], claim['start_y'] + claim['dim_y']):
        for x in range(claim['start_x'], claim['start_x'] + claim['dim_x']):
            if fabric[y][x] > 1:
                return True
    return False


if __name__ == '__main__':
    main()
