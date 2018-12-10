# solution to Advent of Code 2018, day 7 part one and two
# https://adventofcode.com/2018/day/7
#
# Usage: sleigh.py [inputfile]

from collections import defaultdict
import fileinput
import re

def main():
    steplist = set([re.findall(r'\s([A-Z]).*([A-Z])', line).pop() for line in fileinput.input()])

    # graph is a dict of tuples
    # dict key is the name of the step ('A', 'B', 'C', etc)
    # tuple is (set(), set()) where the sets contain inbound
    # and outbound nodes relating to the dict key
    graph = defaultdict(tuplesets)
    INBOUND = 0
    OUTBOUND = 1
    for a, b in steplist:
        graph[a][OUTBOUND].add(b)
        graph[b][INBOUND].add(a)

    # solve part one
    open_nodes = set()
    visited = set()
    steps = ''
    [open_nodes.add(node) for node, related in graph.items() if not related[INBOUND]]

    while open_nodes:
        next_node = min([node for node in open_nodes if graph[node][INBOUND] <= visited])
        open_nodes |= graph[next_node][OUTBOUND]
        steps += next_node
        visited.add(next_node)
        open_nodes.remove(next_node)

    print('Step order:', steps)

    # solve part two
    workers = [None] * 5
    open_nodes = set()
    done = set()
    [open_nodes.add(node) for node, related in graph.items() if not related[INBOUND]]

    seconds = 0
    finished = False
    while not finished:
        finishing_workers = [i for i,worker in enumerate(workers) if not worker == None and worker[0] == seconds]
        for i in finishing_workers:
            finished_step = workers[i][1]
            done.add(finished_step)
            open_nodes |= graph[finished_step][OUTBOUND]
            workers[i] = None

        if len(done) == len(graph.keys()):
            finished = True
            continue
        
        available_workers = [i for i,worker in enumerate(workers) if worker == None]
        if not available_workers:
            seconds += 1
            continue
        for i in available_workers:
            potential_next = [node for node in open_nodes if graph[node][INBOUND] <= done]
            if not potential_next:
                continue
            next_node = min(potential_next)
            workers[i] = ((seconds + ord(next_node) - 4), next_node)
            open_nodes.remove(next_node)
        seconds += 1

    print('Seconds to completion with 5 workers:', seconds)


def tuplesets():
    return (set(), set())


if __name__ == '__main__':
    main()
