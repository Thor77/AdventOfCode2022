#!/bin/env python3

def expand(raw):
    start, end = raw.split('-')
    return range(int(start), int(end) + 1)

def part1(lines):
    duplicate = 0
    for line in lines:
        line_split = line.split(',')
        assignment1 = set(expand(line_split[0]))
        assignment2 = set(expand(line_split[1]))
        if len(assignment1 - assignment2) == 0 or len(assignment2 - assignment1) == 0:
            duplicate += 1
    return duplicate

def part2(lines):
    overlapping = 0
    for line in lines:
        line_split = line.split(',')
        assignment1 = set(expand(line_split[0]))
        assignment2 = set(expand(line_split[1]))
        if assignment1 & assignment2:
            overlapping += 1
    return overlapping

if __name__ == '__main__':
    lines = []
    with open('inputs/04') as f:
        lines = list(map(lambda l: l.replace('\n', ''), f.readlines()))
    print('Part 1:', part1(lines))
    print('Part 2:', part2(lines))
