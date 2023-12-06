with open('data.txt') as f:
    file = f.read().splitlines()

def joined_value(line):
    value = ''
    for i in line.split()[1:]:
        value += i
    return int(value)

time = joined_value(file[0])
distance = joined_value(file[1])

ways = 0
last_s = 0
for i in range(1, time):
    s = i * (time - i)
    if s > distance:
        ways += 1

print(ways)