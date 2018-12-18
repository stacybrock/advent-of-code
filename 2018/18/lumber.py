# solution to Advent of Code 2018, day 18 part one and two
# https://adventofcode.com/2018/day/18
#
# usage: lumber.py [inputfile]

import fileinput

def render(grid):
    for row in grid:
        print(''.join(row))
    print()


def main():
    inputlines = list(line.strip() for line in fileinput.input())

    # parse input
    grid = ['']*len(inputlines)
    for i, line in enumerate(inputlines):
        grid[i] = list(line)

    gridheight = len(grid)
    gridwidth = len(grid[0])

    for minute in range(1000):
        newgrid = [row.copy() for row in grid]
        for y, row in enumerate(grid):
            for x, type in enumerate(grid[y]):
                # get adjacent resources
                adj = []
                for sx in range(-1, 2):
                    for sy in range(-1, 2):
                        if sx == 0 and sy == 0:
                            continue
                        x_ = x + sx
                        y_ = y + sy
                        if x_ in range(gridwidth) and y_ in range(gridheight):
                            adj.append(grid[y_][x_])

                # apply rules
                if grid[y][x] == '.':
                    newgrid[y][x] = '|' if adj.count('|') >= 3 else '.'
                elif grid[y][x] == '|':
                    newgrid[y][x] = '#' if adj.count('#') >= 3 else '|'
                elif grid[y][x] == '#':
                    newgrid[y][x] = '#' if (adj.count('#') >= 1 and adj.count('|') >= 1) else '.'

        grid = [row.copy() for row in newgrid]

        lumberyards = sum([row.count('#') for row in grid])
        woods = sum([row.count('|') for row in grid])
        resources = lumberyards * woods
        if minute + 1 == 10:
            print('Resources after 10 minutes:', resources)
    print('Resources after a billion minutes:', resources)


if __name__ == '__main__':
    import timeit
    print(timeit.timeit('main()', 'from __main__ import main',number=10))
