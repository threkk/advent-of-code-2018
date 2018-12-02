from collections import Counter
from os.path import dirname, join
from itertools import combinations

DIR_PATH = dirname(__file__)
INPUT = join(DIR_PATH, './input.txt')


def part_1():
    with open(INPUT, 'r') as lines:
        counters = [dict(Counter(line)) for line in lines]

        doubles = 0
        triples = 0
        for counter in counters:
            doubles += (1 if len([k for k, v in counter.items() if v == 2]) > 0
                        else 0)
            triples += (1 if len([k for k, v in counter.items() if v == 3]) > 0
                        else 0)

        hash = doubles * triples
        print('+++ PART 1 +++')
        print(f'Hash: {hash}')


def part_2():
    with open(INPUT, 'r') as lines:
        for word_1, word_2 in combinations(lines, 2):
            distance = sum(1 for w1, w2 in zip(word_1, word_2) if w1 != w2)

            if distance == 1:
                common = [w1 for w1, w2 in zip(word_1, word_2) if w1 == w2]
                print('+++ PART 2 +++')
                print(f'Common letters: {"".join(common)}')
                break


if __name__ == '__main__':
    part_1()
    part_2()
