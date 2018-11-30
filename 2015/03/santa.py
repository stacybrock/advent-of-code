# solution to Advent of Code 2015, day 3 part one
# https://adventofcode.com/2015/day/3
#
# assumes puzzle input is in a file called input.txt

houses = {}

def main():
    with open('input.txt') as inputfile:
        directions = inputfile.readline().strip()

        hx = hy = 0
        visit(hx, hy, houses)

        for c in directions:
            if c == '^':
                hy += 1
            elif c == 'v':
                hy -= 1
            elif c == '<':
                hx -= 1
            elif c == '>':
                hx += 1
            else:
                pass
            print(f"Santa is now at {hx},{hy}")
            visit(hx, hy, houses)

    print(count(houses))


def visit(x, y, houses):
    if not x in houses:
        houses[x] = {}

    if y in houses[x]:
        houses[x][y] += 1
    else:
        houses[x][y] = 1


def count(houses):
    counter = 0
    for k, v in houses.items():
        for h in v:
            counter += 1
    return counter


if __name__ == '__main__':
    main()
