with open("data.txt") as f:
    file = f.read().splitlines()

numbers = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
}

def reverse_str(x):
    return x[::-1]

def check_numbers(x):
    for i in numbers:
        if i in x:
            return i
    return ''

sum = 0
for line in file:
    text_number = ''
    result = ''
    for i in range(len(line)):

        try:
            n = int(line[i])
            result+=str(n)
            break
        except Exception:
            pass

        text_number+=line[i]
        check = check_numbers(text_number)
        if check != '':
            result+=str(numbers[check])
            break
    text_number = ''

    for i in range(len(line)-1, -1, -1):
        
        try:
            n = int(line[i])
            result+=str(n)
            break
        except Exception:
            pass

        text_number+=line[i]
        check = check_numbers(reverse_str(text_number))
        if check != '':
            result+=str(numbers[check])
            break
        
    print(result)
    sum+=int(result)

print(f"Sum: {sum}")