# solution to Advent of Code 2018, day 2 part one and two
# https://adventofcode.com/2018/day/2
#
# Usage: inventory.py [inputfile]

import fileinput

def main():
    box_ids = list(line.strip() for line in fileinput.input())

    # solve part one
    two_counts = 0
    three_counts = 0
    for box_id in box_ids:
        two_counts += sum(set([1 for c in set(box_id) if box_id.count(c) == 2]))
        three_counts += sum(set([1 for c in set(box_id) if box_id.count(c) == 3]))
    print(f"Checksum: {two_counts * three_counts}")

    # solve part two
    seen_ids = []
    for box_id in box_ids:
        for seen_id in seen_ids:
            common_letters = [a for a,b in zip(box_id, seen_id) if a == b]
            if len(common_letters) == len(seen_id)-1:
                print(f"Common letters between the correct box IDs: {''.join(common_letters)}")
        seen_ids.append(box_id)


if __name__ == '__main__':
    main()
