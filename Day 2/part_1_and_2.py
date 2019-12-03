
def getInput():
    line = ""
    with open("input", "r") as f:
        line = f.readline()
    splitted = line.strip().split(",")
    intcode = [int(num)for num in splitted]
    return intcode


def calculateIntcodes(intcode):
    first = 0
    while intcode[0+first] != 99:
        if intcode[0 + first] == 1:
            firstOpIndex = intcode[1 + first]
            secondOpIndex = intcode[2 + first]
            finalIndex = intcode[3 + first]
            intcode[finalIndex] = intcode[firstOpIndex] + intcode[secondOpIndex]
        elif intcode[0 + first] == 2:
            firstOpIndex = intcode[1 + first]
            secondOpIndex = intcode[2 + first]
            finalIndex = intcode[3 + first]
            intcode[finalIndex] = intcode[firstOpIndex] * intcode[secondOpIndex]
        else:
            print(intcode[0+first])
            break
        first += 4

def calculate_part1_result():
    intcodes = getInput()
    intcodes[1] = 12
    intcodes[2] = 2
    calculateIntcodes(intcodes)
    return intcodes

def calculate_noun_verb():
    intcodes = getInput()
    intcodes[0] = 0
    intcodes[1] = 0
    for i in range(99):
        for j in range(99):
            intcodes[1] = i
            intcodes[2] = j
            calculateIntcodes(intcodes)
            if intcodes[0] == 19690720:
                break
            else:
                intcodes = getInput()
        if intcodes[0] == 19690720:
            break
    print(intcodes)


            

if __name__ == '__main__':
    calculate_noun_verb()
    