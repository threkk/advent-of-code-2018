from os.path import dirname, join
from re import match
from collections import Counter

DIR_PATH = dirname(__file__)
INPUT = join(DIR_PATH, './input.txt')
EXAMPLE = '''#1 @ 1,3: 4x4
#2 @ 3,1: 4x4
#3 @ 5,5: 2x2
'''

REGEXP = r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)'  # Line format:  #1 @ 1,3: 4x4


def _claims(lines):
    """Returns the squares claimed by every id"""
    blanket = {}
    for line in lines:
        m = match(REGEXP, line)
        groups = [int(group) for group in m.groups()]
        id, left, top, width, height = groups
        squares = [(top + x + 1, left + y + 1) for y in range(0, width) for x
                   in range(0, height)]
        blanket[id] = squares
    return blanket


def part_1(lines):
    blanket = _claims(lines)
    flat_blanket = [square for l in blanket.values() for square in l]
    counters = Counter([f'{x},{y}' for x, y in flat_blanket])

    shared = len([k for k, v in counters.items() if v > 1])
    return shared


def part_2(lines):
    blanket = _claims(lines)
    flat_blanket = [square for l in blanket.values() for square in l]
    counters = Counter([f'{x},{y}' for x, y in flat_blanket])

    shared = [k for k, v in counters.items() if v > 1]
    for id, squares in blanket.items():
        squares_str = [f'{x},{y}' for x, y in squares]
        for square in squares_str:
            if square in shared:
                break
        else:
            return id


if __name__ == '__main__':
    example_lines = EXAMPLE.splitlines()
    assert part_1(example_lines) == 4
    assert part_2(example_lines) == 3

    with open(INPUT, 'r') as lines:
        print('++ PART 1 ++')
        print(part_1(lines))
        print('++ PART 2 ++')
        print(part_2(lines))
