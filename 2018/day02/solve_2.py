def similar_ids_common_letters(box_ids):
    for i in range(len(box_ids)):
        check_id = box_ids.pop()
        for box_id in box_ids:
            diff_idxs = []
            for i in range(len(check_id)):
                if box_id[i] != check_id[i]:
                    diff_idxs.append(i)
                if len(diff_idxs) == 2:
                    continue
            if len(diff_idxs) == 1:
                id_chrs = list(box_id)
                id_chrs.pop(diff_idxs[0])
                return "".join(id_chrs)


def test_similar_ids_common_letters():
    box_ids = [
        'abcde',
        'fghij',
        'klmno',
        'pqrst',
        'fguij',
        'axcye',
        'wvxyz',
    ]

    assert 'fgij' == similar_ids_common_letters(box_ids)


if __name__ == '__main__':
    with open('input_1.txt', 'r') as f:
        box_ids = f.read().split('\n')

    print(similar_ids_common_letters(box_ids))