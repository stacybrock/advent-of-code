# solution to Advent of Code 2018, day 6 part one and two
# https://adventofcode.com/2018/day/6
#
# assumes puzzle input is in a file called input.txt

from collections import defaultdict
from operator import itemgetter

def main():
    with open('input.txt') as inputfile:
        raw_coordinates = list(line.strip() for line in inputfile.readlines())

    # convert 'x, y' formatted coordinates into tuples of ints
    coords = [tuple(map(int,c.split(", "))) for c in raw_coordinates]

    # calculate outer boundary of grid
    min_x = min(coords, key=itemgetter(0))[0]
    max_x = max(coords, key=itemgetter(0))[0]
    min_y = min(coords, key=itemgetter(1))[1]
    max_y = max(coords, key=itemgetter(1))[1]

    # create sets of coordinates that lie on the outer boundary
    leftedge = set([c for c in coords if c[0] == min_x])
    rightedge = set([c for c in coords if c[0] == max_x])
    topedge = set([c for c in coords if c[1] == min_y])
    bottomedge = set([c for c in coords if c[1] == max_y])

    # use set math to determine the coordinates that lie
    # within the outermost edges
    interior_coords = set(coords) - leftedge - rightedge - topedge - bottomedge

    # grid is a dict-of-dicts containing the closest coordinate
    # to that point
    # {0: {0: (x, y)}}
    grid = defaultdict(dict)
    for x in range(min_x, max_x+1):
        for y in range(min_y, max_y+1):
            distances = {}
            for c in coords:
                distances[c] = manhattan_distance((x, y), c)
            (candidate, distance) = min(distances.items(), key=itemgetter(1))
            if list(distances.values()).count(distance) == 1:
                grid[x][y] = candidate
            else:
                grid[x][y] = None

    # solve part one
    coordinate_areas = list(
        [sum([1 for x, y_val in grid.items() for c2 in y_val.values() if c2 == c]) for c in interior_coords]
    )
    print(f"Size of largest area: {max(coordinate_areas)}")

    # solve part two
    grid = defaultdict(dict)
    for x in range(min_x, max_x+1):
        for y in range(min_y, max_y+1):
            total_distance = sum([manhattan_distance((x, y), c) for c in coords])
            if total_distance < 10000:
                grid[x][y] = 1
    area = sum([sum(list(y_val.values())) for x, y_val in grid.items()])
    print(f"Size of < 10000 region: {area}")


def manhattan_distance(a, b):
    """Calculate Manhattan distance between two coordinates
    Inputs:
      a - tuple for point 1
      b - tuple for point 2
    """
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


if __name__ == '__main__':
    main()
