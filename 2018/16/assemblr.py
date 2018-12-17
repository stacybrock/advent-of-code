# solution to Advent of Code 2018, day 16 part one and two
# https://adventofcode.com/2018/day/16
#
# usage: assemblr.py [inputfile]

from collections import defaultdict
import fileinput
import re

def addr(registers, a, b, c):
    result = registers[::]
    result[c] = result[a] + result[b]
    return result

def addi(registers, a, b, c):
    result = registers[::]
    result[c] = result[a] + b
    return result

def mulr(registers, a, b, c):
    result = registers[::]
    result[c] = result[a] * result[b]
    return result

def muli(registers, a, b, c):
    result = registers[::]
    result[c] = result[a] * b
    return result

def banr(registers, a, b, c):
    result = registers[::]
    result[c] = result[a] & result[b]
    return result

def bani(registers, a, b, c):
    result = registers[::]
    result[c] = result[a] & b
    return result

def borr(registers, a, b, c):
    result = registers[::]
    result[c] = result[a] | result[b]
    return result

def bori(registers, a, b, c):
    result = registers[::]
    result[c] = result[a] | b
    return result

def setr(registers, a, b, c):
    result = registers[::]
    result[c] = result[a]
    return result

def seti(registers, a, b, c):
    result = registers[::]
    result[c] = a
    return result

def gtir(registers, a, b, c):
    result = registers[::]
    result[c] = 1 if a > result[b] else 0
    return result

def gtri(registers, a, b, c):
    result = registers[::]
    result[c] = 1 if result[a] > b else 0
    return result

def gtrr(registers, a, b, c):
    result = registers[::]
    result[c] = 1 if result[a] > result[b] else 0
    return result

def eqir(registers, a, b, c):
    result = registers[::]
    result[c] = 1 if a == result[b] else 0
    return result

def eqri(registers, a, b, c):
    result = registers[::]
    result[c] = 1 if result[a] == b else 0
    return result

def eqrr(registers, a, b, c):
    result = registers[::]
    result[c] = 1 if result[a] == result[b] else 0
    return result

def parse(line):
    return list(map(int, re.findall(r'(\d+)', line)))

def main():
    # parse the input into samples and program
    inputlines = list(line.strip() for line in fileinput.input())
    for i, val in enumerate(inputlines):
        if not i+1 >= len(inputlines) and not i+2 > len(inputlines):
            if inputlines[i:i+3] == ['', '', '']:
                samples = inputlines[0:i]
                program = inputlines[i+3:]
                break

    ops = {'addr': addr, 'addi': addi,
           'mulr': mulr, 'muli': muli,
           'banr': banr, 'bani': bani,
           'borr': borr, 'bori': bori,
           'setr': setr, 'seti': seti,
           'gtir': gtir, 'gtri': gtri, 'gtrr': gtrr,
           'eqir': eqir, 'eqri': eqri, 'eqrr': eqrr }

    part1_sample_count = 0
    opcodes = defaultdict(set)

    # solve part one
    for i, line in enumerate(samples):
        if not line.startswith('Before'):
            continue

        before = parse(samples[i])
        inst = parse(samples[i+1])
        after = parse(samples[i+2])
        correct = set()
        for op, func in ops.items():
            reg = before[::]
            reg = func(reg, inst[1], inst[2], inst[3])
            if reg == after:
                correct.add(op)
        if len(correct) >= 3:
            part1_sample_count += 1

        # record correct ops for this sample
        opcodes[inst[0]] |= set(correct)
    print('Samples with 3+ opcodes:', part1_sample_count)

    # solve part two
    # at this point, 'opcodes' contains sets of candidate functions
    # potentially matching each opcode number
    # now winnow the candidates down to the actual function
    while not max([len(c) for op, c in opcodes.items()]) == 1:
        for op, candidates in opcodes.items():
            if not len(candidates) == 1:
                continue
            found_func = list(candidates)[0]
            for op_ in opcodes:
                if op_ == op:
                    continue
                if found_func in opcodes[op_]:
                    opcodes[op_].remove(found_func)

    # convert set into corresponding function
    # opcodes = {0: {'addr'}, 1: {'bori'}, etc into
    # opcodes = {0: <function addr>, 1: <function bori>, etc
    for op, set_ in opcodes.items():
        opcodes[op] = ops[list(set_)[0]]

    # run the program
    reg = [0, 0, 0, 0]
    for line in program:
        inst = parse(line)
        reg = opcodes[inst[0]](reg, inst[1], inst[2], inst[3])
    print('Register 0:', reg[0])


if __name__ == '__main__':
    main()
