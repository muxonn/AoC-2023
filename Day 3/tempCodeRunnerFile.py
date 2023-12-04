
sum = 0
for i in range(len(file)):
    number = ''
    is_number = False
    is_adjacent = False

    for j in range(len(file[i])):
        if file[i][j].isdigit():
            number += file[i][j]
            is_number = True
            if check_adjacents(i,j):
                is_adjacent = True
        else:
            is_number = False

        if is_number == False or j == len(file[i])-1:   
            if is_adjacent:
                print(number)
                sum += int(number)
                is_adjacent = False
            number = ''
        
print(f"Sum: {sum}")