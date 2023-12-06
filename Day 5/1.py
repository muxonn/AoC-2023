import time
start_time = time.time()
with open('data.txt') as f:
    file = f.read().splitlines()

seeds = [i for i in file[0].split()][1:]
maps = []

# Extract data to maps
temp_map = []
for i in file[2:]:
    if i != '':
        temp_map.append(i.split())
    else:
        maps.append(temp_map[1:]) # Append data without header with map name
        temp_map = []
maps.append(temp_map[1:]) # Append data without header with map name
temp_map = []


locations = []
for seed in seeds:
    element = int(seed)
    for one_map in maps:
        for line in one_map:
            if element in range(int(line[1]), int(line[1]) + int(line[2])):
                element = element - int(line[1]) + int(line[0]) # Element = seed - source + destination
                break
    locations.append(element)

print(min(locations))
print("--- %s seconds ---" % (time.time() - start_time))