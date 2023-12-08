with open("data.txt") as f:
    file = f.read().splitlines()

instructions = file[0]
elements = {}

for i in file[2:]:
    element = i.split()
    elements.update({element[0]: [element[2][1:4], element[3][:3]]})

last_nodes = []
for i in elements:
    if i[-1] == 'A':
        last_nodes.append(i)
print(last_nodes)

def check_end(items):
    for i in items:
        if i[-1] != "Z":
            return False
    return True

steps = 0
found = False

while found is False:
    for i in instructions:
        for n, item in enumerate(last_nodes):
            if i == 'L':
                last_nodes[n] = elements[item][0]
            elif i == 'R':
                last_nodes[n] = elements[item][1]

        steps += 1
        if check_end(last_nodes):
            found = True
            break
            
        if steps % 100000 == 0:
            print(steps)
print(steps)