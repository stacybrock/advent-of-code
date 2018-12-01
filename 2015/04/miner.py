# solution to Advent of Code 2015, day 4 part one and two
# https://adventofcode.com/2015/day/4
#
# assumes puzzle input is in a file called input.txt

import hashlib

def main():
    with open('input.txt') as inputfile:
        secret_key = inputfile.readline().strip()

    # solve part one
    (number, md5hash) = mine(secret_key, '00000')
    print(f"Number: {number}\nHash: {md5hash}")

    # solve part two
    (number, md5hash) = mine(secret_key, '000000')
    print(f"Number: {number}\nHash: {md5hash}")


def mine(key, search_prefix):
    number = 1
    while True:
        md5hash = hashlib.md5(f"{key}{number}".encode()).hexdigest()
        if md5hash.startswith(search_prefix):
            return (number, md5hash)
        number += 1


if __name__ == '__main__':
    main()
