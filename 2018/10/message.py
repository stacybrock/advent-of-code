# solution to Advent of Code 2018, day 10 part one and two
# https://adventofcode.com/2018/day/10
#
# usage: message.py [inputfile]

from collections import namedtuple
import fileinput
import re

def main():
    inputlines = list(line.strip() for line in fileinput.input())

    # [(x,y,vx,vy), etc...]
    Point = namedtuple('Point', 'x y vx vy')
    points = []
    for line in [re.findall(r'<(.+),(.+)>.*<(.+),(.+)>', line).pop() for line in inputlines]:
        points.append(Point._make(map(int, line)))

    smallest_width = None
    seconds = 0

    while True:
        min_x = min([p.x for p in points])
        min_y = min([p.y for p in points])
        grid_width = max([p.x for p in points]) - min_x
        grid_height = max([p.y for p in points]) - min_y
        if smallest_width == None or grid_width < smallest_width:
            smallest_width = grid_width
        else:
            break
        offset_x = abs(min_x)
        offset_y = abs(min_y)

        if grid_width < 80:
            grid = [['.']*(grid_width+1) for i in range(grid_height+1)]
            for p in points:
                grid[p.y-offset_y][p.x-offset_x] = '#'
            for row in range(0, grid_height+1):
                print(''.join(grid[row]))
            print(seconds,'seconds')

        for i, p in enumerate(points):
            points[i] = Point(p.x+p.vx, p.y+p.vy, p.vx, p.vy)

        seconds += 1


if __name__ == '__main__':
    main()
