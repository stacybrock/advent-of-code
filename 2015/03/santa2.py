# solution to Advent of Code 2015, day 3 part two
# https://adventofcode.com/2015/day/3
#
# assumes puzzle input is in a file called input.txt

class Distributor:
    # class var for storing visits by Santa and Robo-Santa combined
    houses = {}

    def __init__(self, name):
        self.name = name
        self.hx = self.hy = 0
        print(f"{self.name} starting out at {self.hx},{self.hy}")
        self.visit(0, 0)

    def move(self, direction):
        if direction == '^':
            self.hy += 1
        elif direction == 'v':
            self.hy -= 1
        elif direction == '<':
            self.hx -= 1
        elif direction == '>':
            self.hx += 1
        else:
            pass

        print(f"{self.name} now at {self.hx},{self.hy}")
        self.visit(self.hx, self.hy)

    def visit(self, x, y):
        if not x in self.houses:
            self.houses[x] = {}

        if y in self.houses[x]:
            self.houses[x][y] += 1
        else:
            self.houses[x][y] = 1

    def count_visited(self):
        counter = 0
        for k, v in self.houses.items():
            for h in v:
                counter += 1
        return counter


def main():
    santa = Distributor('Santa')
    robo = Distributor('Robo-Santa')

    with open('input.txt') as inputfile:
        directions = inputfile.readline().strip()

        counter = 0
        for c in directions:
            if counter % 2 == 0:
                santa.move(c)
            else:
                robo.move(c)
            counter += 1

    print(santa.count_visited())


if __name__ == '__main__':
    main()
