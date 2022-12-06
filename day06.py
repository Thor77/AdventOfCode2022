#!/bin/env python3

def find_marker(datastream, uniq_count=4):
    buffer = []
    for i in range(len(datastream)):
        buffer.append(datastream[i])
        if len(buffer) > uniq_count:
            buffer.pop(0)
        if len(buffer) == uniq_count and len(set(buffer)) == uniq_count:
            return i + 1

if __name__ == '__main__':
    datastream = ''
    with open('inputs/06') as f:
        datastream = f.read().rstrip('\n')
    assert find_marker('mjqjpqmgbljsphdztnvjfqwrcgsmlb') == 7
    assert find_marker('bvwbjplbgvbhsrlpgdmjqwftvncz') == 5
    assert find_marker('nppdvjthqldpwncqszvftbrmjlhg') == 6
    print('Part 1:', find_marker(datastream))
    assert find_marker('mjqjpqmgbljsphdztnvjfqwrcgsmlb', uniq_count=14) == 19
    print('Part 2:', find_marker(datastream, uniq_count=14))

