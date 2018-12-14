# solution to Advent of Code 2018, day 14 part one and two
# https://adventofcode.com/2018/day/14
#
# usage: recipes.py [inputfile]

import fileinput

def main():
    instr = next(fileinput.input()).strip()

    # solve part one
    recipes = [3, 7]
    a = 0
    b = 1
    while len(recipes) < int(instr) + 10:
        new = recipes[a] + recipes[b]
        if new >= 10:
            recipes.extend([new // 10, new % 10])
        else:
            recipes.append(new)
        a = (a + 1 + recipes[a]) % len(recipes)
        b = (b + 1 + recipes[b]) % len(recipes)
    print('Next 10 recipe scores:', ''.join(map(str, recipes[-10:])))

    # solve part two
    recipes = [3, 7]
    a = 0
    b = 1
    inchr = [int(c) for c in instr]
    inlen = len(inchr)
    while True:
        new = recipes[a] + recipes[b]
        if new >= 10:
            recipes.extend([new // 10, new % 10])
        else:
            recipes.append(new)
        a = (a + 1 + recipes[a]) % len(recipes)
        b = (b + 1 + recipes[b]) % len(recipes)
        if recipes[-inlen:] == inchr or recipes[-inlen-1:-1] == inchr:
            # check last two groups because 1 or 2 recipes can be added
            # during each loop
            break
    print(f"Number of recipes to the left of '{instr}':", ''.join(map(str, recipes)).index(instr))


if __name__ == '__main__':
    main()
