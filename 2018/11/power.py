# solution to Advent of Code 2018, day 11 part one and two
# https://adventofcode.com/2018/day/11
#
# usage: power.py [inputfile]

from collections import defaultdict
from collections import namedtuple
import fileinput
import numpy

def main():
    serialnumber = int(next(fileinput.input()).strip())

    # create a multidimensional array of power levels at each point
    grid = numpy.zeros((300, 300))
    for (x_,y_), power in numpy.ndenumerate(grid):
        grid[y_][x_] = get_power_level(x_+1, y_+1, serialnumber)

    # solve part one
    threes = defaultdict(int)
    for y in range(0, 298):
        for x in range(0, 298):
            threes[(x+1,y+1)] = numpy.sum(grid[y:y+3, x:x+3])
    print('largest 3x3:', max(threes, key=threes.get))

    # solve part two
    # definitely not as fast as I'd like it to be, but it's
    # an improvement over my first attempts
    squares = defaultdict(int)
    for size in range(1, 301):
        max_power = 0
        Power = namedtuple('Power', 'x y size power')
        for y in range(0, 301-size):
            for x in range(0, 301-size):
                power = numpy.sum(grid[y:y+size, x:x+size])
                if power > max_power:
                    running = Power(x,y,size,power)
                    max_power = power
        squares[(running.x+1, running.y+1, running.size)] = running.power
    print('largest overall:', max(squares, key=squares.get))


def get_power_level(x, y, serial):
    """returns power level for the given x, y, and serial"""
    rack_id = x + 10
    power = (((rack_id*y) + serial) * rack_id)
    if power > 99:
        return (power // 100) % 10 - 5
    else:
        return -5


if __name__ == '__main__':
    main()
