import time
start_time = time.time()

with open('data.txt') as f:
    file = f.read().splitlines()

seeds = []

#Extract data to seeds
# temp_seeds = [i for i in file[0].split()][1:]
# for i in range(0, len(temp_seeds), 2):
#     for j in range(int(temp_seeds[i]), int(temp_seeds[i]) + int(temp_seeds[i+1])):
#         seeds.append(j)

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

seeds = [i for i in file[0].split()][1:]
locations = []

#CHANGE IT
for i in range(0, len(seeds), 2):
    for seed in range(int(seeds[i]), int(seeds[i]) + int(seeds[i+1])):
        element = seed
        for one_map in maps:
            for line in one_map:
                if element in range(int(line[1]), int(line[1]) + int(line[2])):
                    element = element - int(line[1]) + int(line[0]) # Element = seed - source + destination
                    break
        locations.append(element)

print(min(locations))
print("--- %s seconds ---" % (time.time() - start_time))