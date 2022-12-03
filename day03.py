#!/bin/env python3
from string import ascii_letters

def part1(lines):
    priority = 0
    for line in lines:
        half = int(len(line) / 2)
        compartment1 = line[:half]
        compartment2 = line[half:]
        common = (set(compartment1) & set(compartment2)).pop()
        priority += ascii_letters.index(common) + 1
    return priority

def part2(lines):
    priority = 0
    for b1, b2, b3 in zip(*([iter(lines)] * 3)):
        common = set(b1) & set(b2) & set(b3)
        priority += ascii_letters.index(common.pop()) + 1
    return priority

if __name__ == '__main__':
    lines = []
    with open('inputs/03') as f:
        lines = list(map(lambda l: l.replace('\n', ''), f.readlines()))
    print('Part 1:', part1(lines))
    print('Part 2:', part2(lines))
