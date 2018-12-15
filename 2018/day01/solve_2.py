from itertools import cycle


def result_freq_repeats(freq_changes):
    result_freq = 0
    visited_freqs = {result_freq}
    for freq_change in cycle(freq_changes):
        result_freq += int(freq_change)
        if result_freq in visited_freqs:
            return result_freq
        visited_freqs.add(result_freq)


def test_result_freq_repeats():
    input1 = [1, -1]
    input2 = [3, 3, 4, -2, -4]
    assert 0 == result_freq_repeats(input1)
    assert 10 == result_freq_repeats(input2)

if __name__ == '__main__':
    with open('input_1.txt', 'r') as f:
        freq_changes_str = f.read().split('\n')
    freq_changes = [int(freq_change) for freq_change in freq_changes_str]
    print(result_freq_repeats(freq_changes))
