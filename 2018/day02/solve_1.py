from functools import reduce
import operator
from collections import Counter


def get_checksum(box_ids):
    letter_counts = [Counter(box_id) for box_id in box_ids]
    counts = []
    for letter_count in letter_counts:
        counts += set(letter_count.values())
        count_counter = Counter(counts)
        count_counter.pop(1)
    return reduce(operator.mul, count_counter.values(), 1)

def test_get_checksum():
    input_1 = [
        'abcdef',
        'bababc',
        'abbcde',
        'abcccd',
        'aabcdd',
        'abcdee',
        'ababab',
    ]

    assert 12 == get_checksum(input_1)

if __name__ == '__main__':
    with open('input_1.txt', 'r') as f:
        box_ids = f.read().split('\n')
    print(get_checksum(box_ids))
