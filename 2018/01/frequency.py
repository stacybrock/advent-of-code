# solution to Advent of Code 2018, day 1 part one and two
# https://adventofcode.com/2018/day/1
#
# Usage: frequency.py [inputfile]

import fileinput

def main():
    changes = list(map(int, fileinput.input()))

    # solve part one
    current_freq = sum(changes)
    print(f"Resulting frequency: {current_freq}")

    # set up vars for part two
    freqs_seen = set([0])
    current_freq = 0

    # solve part two
    while True:
        for change in changes:
            current_freq += change
            if current_freq in freqs_seen:
                print(f"Found duplicate frequency: {current_freq}")
                return
            freqs_seen.add(current_freq)


if __name__ == '__main__':
    main()
