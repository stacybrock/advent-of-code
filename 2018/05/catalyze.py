# solution to Advent of Code 2018, day 5 part one and two
# https://adventofcode.com/2018/day/5
#
# assumes puzzle input is in a file called input.txt

import string
from operator import itemgetter

def main():
    with open('input.txt') as inputfile:
        polymer = inputfile.readline().strip()

    # solve part one
    print(f"Units in polymer: {catalyze(polymer)}")

    # solve part two
    results = []
    for c in string.ascii_lowercase:
        test_poly = polymer.replace(c, '').replace(c.upper(), '')
        results.append([c, catalyze(test_poly)])
    (letter, units) = min(results, key=itemgetter(1))
    print(f"Removing '{letter}' first results in the shortest length of {units}")


def catalyze(polymer):
    i = 0
    while True:
        while i < len(polymer):
            if i+1 == len(polymer):
                return(len(polymer))
            a = polymer[i]
            b = polymer[i+1]
            if a == b:
                i += 1
                continue
            if a.lower() == b.lower():
                polymer = polymer.replace(f"{a}{b}", '', 1)
                if i != 0:
                    i -= 1
                break
            i += 1


if __name__ == '__main__':
    main()
