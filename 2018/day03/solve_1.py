import re


def find_overlap(input_text):
    fabrics = re.findall('#\d+ @ (\d+),(\d+): (\d+)x(\d+)', input_text)
    covered_points = set()
    overlap_points = set()
    for fabric in fabrics:
        fabric = [int(p) for p in fabric]
        for point in generate_points(fabric):
            if point not in covered_points:
                covered_points.add(point)
            else:
                overlap_points.add(point)
    return len(overlap_points)


def generate_points(fabric):
    for x in range(fabric[0], fabric[2] + fabric[0]):
        for y in range(fabric[1], fabric[3] + fabric[1]):
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