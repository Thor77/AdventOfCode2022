#!/bin/env python3
import copy
import re
from collections import namedtuple
from itertools import groupby

Instruction = namedtuple('Instruction', ['amount', 'origin', 'target'])


def part1(stacks, instructions):
    for instruction in instructions:
        for _ in range(instruction.amount):
            stacks[instruction.target - 1].insert(0, stacks[instruction.origin - 1].pop(0))
    return ''.join(map(lambda s: s[0], stacks))

def part2(stacks, instructions):
    for instruction in instructions:
        grab = []
        for _ in range(instruction.amount):
            grab.append(stacks[instruction.origin - 1].pop(0))
        stacks[instruction.target - 1] = grab + stacks[instruction.target - 1]
    return ''.join(map(lambda s: s[0], stacks))

if __name__ == '__main__':
    stacks = []
    instructions = []
    stack_re = re.compile(r'\ *\[(\w)\]')
    stack_label_re = re.compile(r'\d')
    instruction_re = re.compile(r'move (\d+) from (\d+) to (\d+)')
    with open('inputs/05') as f:
        stacks_raw, instructions_raw = f.read().split('\n\n')
        # parse stack
        matches = []
        stacks_raw_lines = stacks_raw.splitlines()
        for line in stacks_raw_lines:
            pos = 0
            while True:
                match = stack_re.match(line, pos)
                if not match:
                    break
                matches.append(match)
                pos = match.span()[1] + 1
        stack_count = len(stack_label_re.findall(stacks_raw_lines[-1]))
        span_key = lambda m: m.span()[1]
        for _, matches in groupby(sorted(matches, key=span_key), span_key):
            stacks.append(list(map(lambda m: m.group(1), matches)))

        # parse instructions
        instructions = list(map(
            lambda i: Instruction(*map(int, instruction_re.match(i).groups())),
            instructions_raw.splitlines()
        ))
    print('Part 1:', part1(copy.deepcopy(stacks), instructions))
    print('Part 2:', part2(copy.deepcopy(stacks), instructions))
