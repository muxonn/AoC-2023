with open("data.txt") as f:
    file = f.read().splitlines()

color_set = {
    'red': 12,
    'green': 13,
    'blue': 14,
}

id = 0
sum = 0
possible_games = 0
for i in file:
    data = i.split(':')
    sets = data[1].split()
    id += 1
    possible_games+=id

    for j in range(0, len(sets)-1, 2):
        value = int(sets[j])
        color = sets[j+1]
        if color[-1] == ',' or color[-1] == ';':
            color = color[:-1]
        if(value > color_set[color]):
            sum += id
            break

possible_games = possible_games - sum

print(f"Sum: {possible_games}")