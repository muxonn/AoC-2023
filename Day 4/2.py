with open('data.txt') as f:
    file = f.read().splitlines()

winning = []
owned = []

# Recursive function that gets points from duplicates of cards
def get_points(line):
    points = 1
    x = line
    for i in owned[line]:
        if i in winning[line]:
            x+=1
            points += get_points(x)
        
    return points


# Extracting file lines to winning and owned arrays
for i in file:
    line = i.split()
    current_winning = []
    current_owned = []
    isWinning = True
    for j in range(2, len(line)):
        if line[j] == '|':
            isWinning = False
            continue

        if isWinning:
            current_winning.append(line[j])
        else:
            current_owned.append(line[j])
    winning.append(current_winning)
    owned.append(current_owned)

sum = 0
for i in range(len(file)):
    sum += get_points(i)

print(sum)