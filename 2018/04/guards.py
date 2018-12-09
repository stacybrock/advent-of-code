# solution to Advent of Code 2018, day 4 part one and two
# https://adventofcode.com/2018/day/4
#
# Usage: guards.py [inputfile]

import fileinput
import re
from collections import defaultdict
from operator import itemgetter

def main():
    observations = list(line.strip() for line in fileinput.input())

    # a dict-of-dicts mapping guard ids to sleep amounts by minute
    # {id: {minute: 0}}
    guard_records = {}

    current_guard = 0
    prev_action_minute = 0
    for ob in sorted(observations):
        match = re.search(r'#(\d+?) begins', ob)
        if match:
            current_guard = int(match.group(1))
            if not current_guard in guard_records:
                guard_records[current_guard] = defaultdict(int)
            continue

        match = re.search(r':(\d+)] (.*)', ob)
        if match:
            minute = int(match.group(1))
            text = match.group(2)

            if text == 'falls asleep':
                prev_action_minute = minute
                continue

            if text == 'wakes up':
                for i in range(prev_action_minute, minute):
                    guard_records[current_guard][i] += 1
                prev_action_minute = minute

    # solve part one
    sleepiest_guard = max([(guard, sum(sleep.values())) for guard, sleep in guard_records.items()], key=itemgetter(1))[0]
    sleepiest_minute = max(guard_records[sleepiest_guard], key=guard_records[sleepiest_guard].get)
    print(f"Strategy 1 result: {sleepiest_guard * sleepiest_minute}")

    # solve part two
    sleepiest_by_minute = []
    for minute in range(0, 60):
        sleepiest_by_minute.append(max([(minute, guard, sleep[minute]) for guard, sleep in guard_records.items()], key=itemgetter(2)))
    (minute, sleepiest_guard, sleep_amount) = max(sleepiest_by_minute, key=itemgetter(2))
    print(f"Strategy 2 result: {sleepiest_guard * minute}")


if __name__ == '__main__':
    main()
