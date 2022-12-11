#!/bin/env python3
def part1(rows, columns):
    visible = 0
    for row_idx, row in enumerate(rows):
        for tree_idx, tree in enumerate(row):
            column = columns[tree_idx]
            left_trees = row[:tree_idx]
            max_left = max(left_trees) if left_trees else None
            right_trees = row[(tree_idx + 1):]
            max_right = max(right_trees) if right_trees else None
            top_trees = column[:row_idx]
            max_top = max(top_trees) if top_trees else None
            bottom_trees = column[(row_idx + 1):]
            max_bottom = max(bottom_trees) if bottom_trees else None
            if None in [max_left, max_right, max_top, max_bottom] \
                    or max_left < tree or max_right < tree or max_top < tree or max_bottom < tree:
                visible += 1
    return visible

def viewing_distance(current_tree, trees):
    result = 0
    for tree in trees:
        if current_tree > tree:
            result += 1
        else:
            # add the tree the view is blocked by
            result += 1
            break
    return result

def part2(rows, columns):
    max_score = 0
    for row_idx, row in enumerate(rows):
        for tree_idx, tree in enumerate(row):
            column = columns[tree_idx]
            left_trees = row[:tree_idx]
            vdistance_left = viewing_distance(tree, reversed(left_trees))
            right_trees = row[(tree_idx + 1):]
            vdistance_right = viewing_distance(tree, right_trees)
            top_trees = column[:row_idx]
            vdistance_top = viewing_distance(tree, reversed(top_trees))
            bottom_trees = column[(row_idx + 1):]
            vdistance_bottom = viewing_distance(tree, bottom_trees)
            score = vdistance_left * vdistance_right * vdistance_top * vdistance_bottom
            if score > max_score:
                max_score = score
    return max_score

if __name__ == '__main__':
    rows = []
    with open('inputs/08') as f:
        for row in f.readlines():
            row = row.rstrip('\n')
            rows.append(list(map(int, row)))
    columns = [list(row) for row in zip(*rows)]
    print('Part 1:', part1(rows, columns))
    print('Part 2:', part2(rows, columns))
