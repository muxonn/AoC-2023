
histories = []

for line in open('data.txt'):
    extracted = []
    char = ''
    for i in line.split():
        if i == '-':
            char = i
            continue
        
        extracted.append(int(char + i))
        char = ''
        
    histories.append(extracted)

total = 0

for line in histories:
    sequences = line
    last_values = []
    while all(i == 0 for i in sequences) == False:
        last_values.append(sequences[-1])
        current_sequences = []
        for n in range(1, len(sequences)):
            current_sequences.append(sequences[n] - sequences[n-1])
        sequences = current_sequences
        
    for value in last_values:
        total += value

print(total)
    