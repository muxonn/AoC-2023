with open("data.txt") as f:
    file = f.read().splitlines()

sum = 0
for line in file:
    result = ''
    for i in range(len(line)):
        try:
            n = int(line[i])
            result+=str(n)
            break
        except Exception:
            pass

    for i in range(len(line)-1, -1, -1):
        try:
            n = int(line[i])
            result+=str(n)
            break
        except Exception:
            pass
        
    print(result)
    sum+=int(result)

print(f"Sum: {sum}")