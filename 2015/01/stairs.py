# solution to Advent of Code 2015, day 1 part one and two
# https://adventofcode.com/2015/day/1
#
# assumes puzzle input is in a file called input.txt

def main():
    with open('input.txt') as inputfile:
        directions = inputfile.readline().strip()

    current_floor = 0
    c_position = 1
    entered_basement = False

    for c in directions:
        if c == '(':
            current_floor += 1
        elif c == ')':
            current_floor -= 1
        else:
            pass

        if entered_basement == False and current_floor == -1:
            entered_basement = True
            print(f"First entered basement at position {c_position}")
        else:
            c_position += 1

    print(f"Santa is on floor {current_floor}")


if __name__ == '__main__':
    main()
