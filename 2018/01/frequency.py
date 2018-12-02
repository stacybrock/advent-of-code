# solution to Advent of Code 2018, day 1 part one and two
# https://adventofcode.com/2018/day/1
#
# assumes puzzle input is in a file called input.txt

def main():
    # get list of freq changes from input
    changes = []
    with open('input.txt') as inputfile:
        changes = list(map(int, inputfile.readlines()))

    # solve part one
    current_freq = sum(changes)
    print(f"Resulting frequency: {current_freq}")

    # set up vars for part two
    freqs_seen = []
    freqs_seen.append(0)
    current_freq = 0

    # solve part two
    while True:
        for change in changes:
            current_freq += change
            if current_freq in freqs_seen:
                print(f"Found duplicate frequency: {current_freq}")
                return
            freqs_seen.append(current_freq)


if __name__ == '__main__':
    main()
