#!/bin/env python3
from collections import namedtuple

Movement = namedtuple('Movement', ['direction', 'distance'])

def print_grid(visited_positions):
    for y in reversed(range(5)):
        for x in range(6):
            if (x, y) in visited_positions:
                print('#', end='')
            else:
                print('.', end='')
        print()

def part1(movements):
    head_position = [0, 0] # x, y
    tail_position = [0, 0]
    tail_positions = set()
    tail_positions.add(tuple(tail_position))
    for movement in movements:
        print(movement)
        # change head position
        for _ in range(movement.distance):
            # could define function for each direction
            # instead of using match for every step
            match movement.direction:
                case 'R':
                    head_position[0] += 1
                case 'U':
                    head_position[1] += 1
                case 'L':
                    head_position[0] -= 1
                case 'D':
                    head_position[1] -= 1
            print(head_position, tail_position, end='')
            if head_position[0] != tail_position[0] and head_position[1] != tail_position[1]:
                print(' diag', end='')
                # diagonal movements
                if head_position[1] - tail_position[1] > 1:
                    # move up
                    if head_position[0] > tail_position[0]:
                        # move up right
                        tail_position[0] += 1
                        tail_position[1] += 1
                        print(' ur', end='')
                    elif head_position[0] < tail_position[0]:
                        # move up left
                        tail_position[0] -= 1
                        tail_position[1] += 1
                        print(' ul', end='')
                elif head_position[1] - tail_position[1] < -1:
                    # move down
                    if head_position[0] > tail_position[0]:
                        # move down right
                        tail_position[0] += 1
                        tail_position[1] -= 1
                        print(' dr', end='')
                    elif head_position[0] < tail_position[0]:
                        # move down left
                        tail_position[0] -= 1
                        tail_position[1] -= 1
                        print(' dl', end='')
                elif head_position[0] - tail_position[0] > 1:
                    # move right
                    if head_position[1] > tail_position[1]:
                        # move right up
                        tail_position[0] += 1
                        tail_position[1] += 1
                        print(' ru', end='')
                    elif head_position[1] < tail_position[1]:
                        # move right down
                        tail_position[0] += 1
                        tail_position[1] -= 1
                        print(' rd', end='')
                elif head_position[0] - tail_position[0] < -1:
                    # move left
                    if head_position[1] > tail_position[1]:
                        # move left up
                        tail_position[0] -= 1
                        tail_position[1] += 1
                        print(' lu', end='')
                    elif head_position[1] < tail_position[1]:
                        # move left down
                        tail_position[0] -= 1
                        tail_position[1] -= 1
                        print(' ld', end='')
            else:
                print(' plain', end='')
                # plain movements
                if head_position[0] - tail_position[0] > 1:
                    # move tail right
                    tail_position[0] += 1
                elif head_position[1] - tail_position[1] > 1:
                    # move tail up
                    tail_position[1] += 1
                elif head_position[0] - tail_position[0] < -1:
                    # move tail left
                    tail_position[0] -= 1
                elif head_position[1] - tail_position[1] < -1:
                    # move tail down
                    tail_position[1] -= 1
            # record tail position
            print('', tail_position)
            tail_positions.add(tuple(tail_position))
        print_grid(tail_positions)
    print(tail_positions)
    return len(tail_positions)

if __name__ == '__main__':
    movements = []
    with open('inputs/09') as f:
        for line in f.readlines():
            line = line.rstrip('\n')
            direction, distance = line.split()
            movements.append(Movement(direction, int(distance)))
    print('Part 1:', part1(movements))
    # 7131 too high
