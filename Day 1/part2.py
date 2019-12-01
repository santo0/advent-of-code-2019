def sum_extra_fuel(n):
    num = int(n / 3) - 2
    if (num <= 0):
        return 0
    return num + sum_extra_fuel(num)

total = 0

with open("input","r") as f:
    line = f.readline()
    while line:
        total += sum_extra_fuel(int(line))
        line = f.readline()

print(total)