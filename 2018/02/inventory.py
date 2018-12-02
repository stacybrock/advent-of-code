# solution to Advent of Code 2018, day 2 part one and two
# https://adventofcode.com/2018/day/2
#
# assumes puzzle input is in a file called input.txt

def main():
    with open('input.txt') as inputfile:
        box_ids = list(line.strip() for line in inputfile.readlines())

    # solve part one
    two_counts = three_counts = 0
    for box_id in box_ids:
        uniq_chars = set(box_id)

        for char in uniq_chars:
            if box_id.count(char) == 2:
                two_counts += 1
                break

        for char in uniq_chars:
            if box_id.count(char) == 3:
                three_counts += 1
                break

    print(f"Checksum: {two_counts * three_counts}")

    # solve part two
    seen_ids = []
    for box_id in box_ids:
        for seen_id in seen_ids:
            differences = sum(1 for a, b in zip(box_id, seen_id) if a != b)
            if differences == 1:
                common_letters = ''.join(list(a for a, b in zip(box_id, seen_id) if a == b))
                print(f"Common letters between the correct box IDs: {common_letters}")
        seen_ids.append(box_id)


if __name__ == '__main__':
    main()
