with open('data.txt') as f:
    file = f.read().splitlines()

time = [int(i) for i in file[0].split()[1:]]
distance = [int(i) for i in file[1].split()[1:]]

total = 1
for i in range(len(time)):
    ways = 0
    for j in range(1,time[i]):
        s = j * ( time[i] - j)
        if s > distance[i]:
            ways += 1
    total *= ways

print(total)
