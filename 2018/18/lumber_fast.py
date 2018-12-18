# solution to Advent of Code 2018, day 18 part one and two
# https://adventofcode.com/2018/day/18
#
# usage: lumber_fast.py [inputfile]

import fileinput

def render(grid):
    for i, line in enumerate(grid):
        print(''.join(grid[i]))
    print()


def get_adjacent(grid, x, y, gridwidth, gridheight):
    adj = []
    if y == 0:
        if x == 0:
            adj.append(grid[y][x+1])
            adj.extend(grid[y+1][x:x+2])
        elif x == gridwidth - 1:
            adj.append(grid[y][x-1])
            adj.extend(grid[y+1][x-1:x+1])
        else:
            adj.extend([grid[y][x-1], grid[y][x+1]])
            adj.extend(grid[y+1][x-1:x+2])
    elif y == gridheight - 1:
        if x == 0:
            adj.append(grid[y][x+1])
            adj.extend(grid[y-1][x:x+2])
        elif x == gridwidth - 1:
            adj.append(grid[y][x-1])
            adj.extend(grid[y-1][x-1:x+1])
        else:
            adj.extend([grid[y][x-1], grid[y][x+1]])
            adj.extend(grid[y-1][x-1:x+2])
    else:
        if x == 0:
            adj.extend(grid[y-1][x:x+2])
            adj.append(grid[y][x+1])
            adj.extend(grid[y+1][x:x+2])
        elif x == gridwidth - 1:
            adj.append(grid[y][x-1])
            adj.extend(grid[y-1][x-1:x+1])
            adj.extend(grid[y+1][x-1:x+1])
        else:
            adj.extend(grid[y-1][x-1:x+2])
            adj.extend([grid[y][x-1], grid[y][x+1]])
            adj.extend(grid[y+1][x-1:x+2])
    return adj


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
                adj = get_adjacent(grid, x, y, gridwidth, gridheight)

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
