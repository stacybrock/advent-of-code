# solution to Advent of Code 2018, day 13 part one and two
# https://adventofcode.com/2018/day/13
#
# usage: minecart.py [inputfile]

from collections import namedtuple
from operator import attrgetter
import fileinput

def main():
    inputlines = list([line.rstrip() for line in fileinput.input()])

    Point = namedtuple('Point', 'x y')
    Cart = namedtuple('Cart', 'facing turning')
    track = {}
    carts = {}

    for y, line in enumerate(inputlines):
        for x, c in enumerate(line):
            if c in ['v', '^']:
                track[Point(x, y)] = '|'
                carts[Point(x, y)] = Cart(c, 'left')
                continue
            elif c in ['>', '<']:
                track[Point(x, y)] = '-'
                carts[Point(x, y)] = Cart(c, 'left')
                continue
            elif c == ' ':
                continue
            else:
                track[Point(x, y)] = c

    Move = namedtuple('Move', 'x y')
    move = {'v': Move(0, 1), '^': Move(0, -1), '>': Move(1, 0), '<': Move(-1, 0)}
    left_turn = {'>': '^', '^': '<', '<': 'v', 'v': '>'}
    right_turn = {'>': 'v', 'v': '<', '<': '^', '^': '>'}
    next_turn = {'left': 'straight', 'straight': 'right', 'right': 'left'}
    forwardslash_turn = {'>': '^', '^': '>', '<': 'v', 'v': '<'}
    backslash_turn = {'>': 'v', 'v': '>', '<': '^', '^': '<'}

    part1 = None
    while True:
        cart_locations = sorted(carts, key=attrgetter('y', 'x'))
        for loc in cart_locations:
            if not loc in carts:
                continue
            cart = carts[loc]
            offset = move[cart.facing]
            next_loc = Point(loc.x+offset.x, loc.y+offset.y)

            new_turning = cart.turning
            if track[next_loc] == '\\':
                new_facing = backslash_turn[cart.facing]
            elif track[next_loc] == '/':
                new_facing = forwardslash_turn[cart.facing]
            elif track[next_loc] == '+':
                if cart.turning == 'left':
                    new_facing = left_turn[cart.facing]
                elif cart.turning == 'right':
                    new_facing = right_turn[cart.facing]
                else:
                    new_facing = cart.facing
                new_turning = next_turn[cart.turning]
            else:
                (new_facing, new_turning) = (cart.facing, cart.turning)
            new_cart = Cart(new_facing, new_turning)

            if next_loc in carts:
                part1 = part1 or (next_loc.x, next_loc.y)
                del carts[next_loc]
            else:
                carts[next_loc] = new_cart
            del carts[loc]

        if len(carts) == 1:
            part2 = [(p.x, p.y) for p, c in carts.items()].pop()
            break

    print('First collision:', part1)
    print('Last cart left:', part2)
                

if __name__ == '__main__':
    main()
