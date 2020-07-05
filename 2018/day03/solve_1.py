import re
from collections import namedtuple


fabric = namedtuple('fabric', ['id', 'x', 'y', 'width', 'length'])

def find_overlap(input_text):
    fabrics = re.findall('#(\d+) @ (\d+),(\d+): (\d+)x(\d+)', input_text)
    covered_points = set()
    overlap_points = set()
    for f in fabrics:
        f = fabric(*(int(p) for p in f))
        for point in generate_points(f):
            if point not in covered_points:
                covered_points.add(point)
            else:
                overlap_points.add(point)
    return overlap_points


def generate_points(fabric):
    for x in range(fabric.x, fabric.x + fabric.width):
        for y in range(fabric.y, fabric.y + fabric.length):
            yield x, y


def test_find_overlap():
    input_text = """
        #1 @ 1,3: 4x4
        #2 @ 3,1: 4x4
        #3 @ 5,5: 2x2
        """
    assert 4 == find_overlap(input_text)


if __name__ == '__main__':
    with open('input_1.txt', 'r') as f:
        input_text = f.read()
    print(find_overlap(input_text))