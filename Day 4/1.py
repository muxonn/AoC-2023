with open('data.txt') as f:
    file = f.read().splitlines()

total_points = 0
for i in file:
    line = i.split()
    winning = []
    owned = []
    isWinning = True
    for j in range(2, len(line)):
        if line[j] == '|':
            isWinning = False
            continue

        if isWinning:
            winning.append(line[j])
        else:
            owned.append(line[j])
    print(line[1], winning, owned)

    points = 0
    first = True
    for n in owned:
        if n in winning:
            if first:
                points = 1
                first = False
            else:
                points = points*2
    total_points += points

print(total_points)