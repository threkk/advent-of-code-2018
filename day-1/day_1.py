from os.path import dirname, join
from itertools import cycle

FILE_DIR = dirname(__file__)
INPUT = join(FILE_DIR, './input.txt')


def part1():
    print('++ PART 1 ++')
    with open(INPUT, 'r') as lines:
        total = sum([int(line) for line in lines])

        print(f"total: {total}")


def part2():
    print('++ PART 2 ++')

    with open(INPUT, 'r') as lines:
        total = 0
        seen = {0}
        # We need to cycle several times.
        changes = cycle([int(line) for line in lines])

        while True:
            total += next(changes)

            if total in seen:
                print(f'First duplicated value: {total}')
                break
            else:
                seen.add(total)


if __name__ == '__main__':
    part1()
    part2()
