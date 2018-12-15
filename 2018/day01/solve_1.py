with open('input_1.txt', 'r') as f:
    freq_changes = f.read().split('\n')

print(sum([int(freq_change) for freq_change in freq_changes]))
