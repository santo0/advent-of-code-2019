total = 0
with open("input", "r") as f:
    line = f.readline()
    while line:
        num = int(line)
        total += int(num / 3) - 2
        line = f.readline()
print(total)
