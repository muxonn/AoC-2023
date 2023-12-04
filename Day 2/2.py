with open("data.txt") as f:
    file = f.read().splitlines()


id = 0
sum = 0
for i in file:
    data = i.split(':')
    sets = data[1].split()
    id += 1
    color_set = {
    'red': 0,
    'green': 0,
    'blue': 0,
    }

    for j in range(0, len(sets)-1, 2):
        value = int(sets[j])
        color = sets[j+1]
        if color[-1] == ',' or color[-1] == ';':
            color = color[:-1]
        if(value > color_set[color]):
            color_set[color] = value
    power = color_set['red'] * color_set['green'] * color_set['blue']
    sum += power

print(f'Sum: {sum}')