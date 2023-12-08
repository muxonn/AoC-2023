with open("data.txt") as f:
    file = f.read().splitlines()

instructions = file[0]
elements = {}

for i in file[2:]:
    element = i.split()
    elements.update({element[0]: [element[2][1:4], element[3][:3]]})


steps = 0
last = 'AAA'
found = False

while found is False:
    for i in instructions:
        if i == 'L':
            last = elements[last][0]
        elif i == 'R':
            last = elements[last][1]
        steps += 1
        if last == 'ZZZ':
            found = True
            break
print(steps)