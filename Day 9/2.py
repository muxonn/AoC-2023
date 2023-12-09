
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
    first_values = []
    while all(i == 0 for i in sequences) == False:
        first_values.append(sequences[0])
        current_sequences = []
        for n in range(1, len(sequences)):
            current_sequences.append(sequences[n] - sequences[n-1])
        sequences = current_sequences

    previous = 0
    for value in first_values[::-1]:
        previous = value - previous

    total += previous

print(total)
    