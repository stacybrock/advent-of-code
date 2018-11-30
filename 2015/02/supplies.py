# solution to Advent of Code 2015, day 2 part one and two
# https://adventofcode.com/2015/day/2
#
# assumes puzzle input is in a file called input.txt

def main():
    total_sqft = 0
    total_ribbon = 0

    with open('input.txt') as inputfile:
        for line in inputfile:
            (l, w, h) = map(int, line.split('x'))

            a = l*w
            b = w*h
            c = h*l

            sqft = 2*a + 2*b + 2*c + min(a, b, c)
            total_sqft += sqft

            a_perimeter = 2*l + 2*w
            b_perimeter = 2*w + 2*h
            c_perimeter = 2*h + 2*l

            ribbon = min(a_perimeter, b_perimeter, c_perimeter) + l*w*h
            print(f"{l}x{w}x{h} needs {sqft} sqft and {ribbon} ribbon")
            total_ribbon += ribbon

    print(f"Total wrapping paper needed: {total_sqft}")
    print(f"Total ribbon needed: {total_ribbon}")


if __name__ == '__main__':
    main()
