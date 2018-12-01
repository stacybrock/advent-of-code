import os
from pathlib import Path
import requests

def main():
    cwd = Path.cwd()
    day = int(cwd.parts[-1])
    year = cwd.parts[-2]

    aoc_url = f"https://adventofcode.com/{year}/day/{day}/input"
    print(f"Getting puzzle input from {aoc_url}...")

    cookies = {'session': os.getenv('AOC_SESSION')}

    r = requests.get(aoc_url, cookies=cookies)
    with open('input.txt', 'w') as outputfile:
        outputfile.write(r.text.strip())


if __name__ == '__main__':
    main()
