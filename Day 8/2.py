import math

with open("data.txt") as f:
    file = f.read().splitlines()

instructions = file[0]
elements = {}

for i in file[2:]:
    element = i.split()
    elements.update({element[0]: [element[2][1:4], element[3][:3]]})

start_nodes = []
for i in elements:
    if i[-1] == 'A':
        start_nodes.append(i)
print(start_nodes)

all_steps = []
for item in start_nodes:
    last = item
    steps = 0
    found = False
    while found is False:
        for i in instructions:
            if i == 'L':
                last = elements[last][0]
            elif i == 'R':
                last = elements[last][1]
            steps += 1
            if last[-1] == 'Z':
                all_steps.append(steps)
                found = True
                break

def find_lcm_of_list(numbers):
    lcm = numbers[0]
    for num in numbers[1:]:
        lcm = math.lcm(lcm, num)
    return lcm

print(find_lcm_of_list(all_steps))