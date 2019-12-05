from collections import namedtuple

INPUT_VALUE = 5


def getInput():
    line = ""
    with open("input", "r") as f:
        line = f.readline()
    splitted = line.strip().split(",")
    intcode = [int(num)for num in splitted]
    return intcode


ThreeParam = namedtuple('ThreeParam', 'p1 p2 p3', defaults=(0,)*3)
TwoParam = namedtuple('TwoParam', 'p1 p2', defaults=(0,)*2)
OneParam = namedtuple('OneParam', 'p1', defaults=(0,))


def calculateIntcodes(intcode):
    try:
        i0 = 0
        while i0 < len(intcode):
            if len(str(intcode[i0])) != 1:
                op_code = int(str(intcode[i0])[-2:])
            else:
                op_code = intcode[i0]
            if op_code == 1:
                mode = get_mode(intcode, i0)
                i1 = intcode[intcode[i0 + 1]
                             ] if mode.p1 == 0 else intcode[i0 + 1]
                i2 = intcode[intcode[i0 + 2]
                             ] if mode.p2 == 0 else intcode[i0 + 2]
                i3 = intcode[i0 + 3]
                intcode[i3] = i1 + i2
                i0 += 4
            elif op_code == 2:
                mode = get_mode(intcode, i0)
                i1 = intcode[intcode[i0 + 1]
                             ] if mode.p1 == 0 else intcode[i0 + 1]
                i2 = intcode[intcode[i0 + 2]
                             ] if mode.p2 == 0 else intcode[i0 + 2]
                i3 = intcode[i0 + 3]
                intcode[i3] = i1 * i2
                i0 += 4
            elif op_code == 3:
                mode = get_mode(intcode, i0)
                i1 = intcode[i0 + 1] if mode.p1 == 0 else intcode[i0 + 1]
                intcode[i1] = INPUT_VALUE
                i0 += 2
            elif op_code == 4:
                mode = get_mode(intcode, i0)
                i1 = intcode[intcode[i0 + 1]
                             ] if mode.p1 == 0 else intcode[i0 + 1]
                print("--->op 4<---", i1, i0 + 1)
                i0 += 2
            elif op_code == 5:
                mode = get_mode(intcode, i0)
                i1 = intcode[intcode[i0 + 1]
                             ] if mode.p1 == 0 else intcode[i0 + 1]
                i2 = intcode[intcode[i0 + 2]
                             ] if mode.p2 == 0 else intcode[i0 + 2]
                if i1 != 0:
                    i0 = i2
                else:
                    i0 += 3
            elif op_code == 6:
                mode = get_mode(intcode, i0)
                i1 = intcode[intcode[i0 + 1]
                             ] if mode.p1 == 0 else intcode[i0 + 1]
                i2 = intcode[intcode[i0 + 2]
                             ] if mode.p2 == 0 else intcode[i0 + 2]
                if i1 == 0:
                    i0 = i2
                else:
                    i0 += 3
            elif op_code == 7:
                mode = get_mode(intcode, i0)
                i1 = intcode[intcode[i0 + 1]
                             ] if mode.p1 == 0 else intcode[i0 + 1]
                i2 = intcode[intcode[i0 + 2]
                             ] if mode.p2 == 0 else intcode[i0 + 2]
                i3 = intcode[i0 + 3]
                intcode[i3] = 1 if i1 < i2 else 0
                i0 += 4
            elif op_code == 8:
                mode = get_mode(intcode, i0)
                i1 = intcode[intcode[i0 + 1]
                             ] if mode.p1 == 0 else intcode[i0 + 1]
                i2 = intcode[intcode[i0 + 2]
                             ] if mode.p2 == 0 else intcode[i0 + 2]
                i3 = intcode[i0 + 3]
                intcode[i3] = 1 if i1 == i2 else 0
                i0 += 4
            else:
                print("shouldn't happen", i0, op_code)
                break
            print("--------------------")
    except IndexError:
        print("ha petao")
        print(i0)


def get_mode(intcode, i0):
    op_code = int(str(intcode[i0])[-2:])
    op_params = str(intcode[i0])[:-2][::-1]
    if 1 == op_code or 2 == op_code or 7 == op_code or 8== op_code:
        fields = tuple(int(d) for d in op_params)
        return ThreeParam(*fields) if 0 < len(op_params) else ThreeParam()
    elif 3 == op_code or 4 == op_code:
        return OneParam(op_params[0]) if 0 < len(op_params) else OneParam()
    elif 5 == op_code or 6 == op_code:
        fields = tuple(int(d) for d in op_params)
        return TwoParam(*fields) if 0 < len(op_params) else TwoParam()
    else:
        print("this shouldn't happen")


if __name__ == '__main__':
    #my_input = getInput()
    my_input = [int(d)for d in "3,225,1,225,6,6,1100,1,238,225,104,0,1101,72,36,225,1101,87,26,225,2,144,13,224,101,-1872,224,224,4,224,102,8,223,223,1001,224,2,224,1,223,224,223,1102,66,61,225,1102,25,49,224,101,-1225,224,224,4,224,1002,223,8,223,1001,224,5,224,1,223,224,223,1101,35,77,224,101,-112,224,224,4,224,102,8,223,223,1001,224,2,224,1,223,224,223,1002,195,30,224,1001,224,-2550,224,4,224,1002,223,8,223,1001,224,1,224,1,224,223,223,1102,30,44,225,1102,24,21,225,1,170,117,224,101,-46,224,224,4,224,1002,223,8,223,101,5,224,224,1,224,223,223,1102,63,26,225,102,74,114,224,1001,224,-3256,224,4,224,102,8,223,223,1001,224,3,224,1,224,223,223,1101,58,22,225,101,13,17,224,101,-100,224,224,4,224,1002,223,8,223,101,6,224,224,1,224,223,223,1101,85,18,225,1001,44,7,224,101,-68,224,224,4,224,102,8,223,223,1001,224,5,224,1,223,224,223,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,7,677,226,224,102,2,223,223,1005,224,329,101,1,223,223,8,677,226,224,1002,223,2,223,1005,224,344,1001,223,1,223,1107,677,677,224,102,2,223,223,1005,224,359,1001,223,1,223,1107,226,677,224,102,2,223,223,1005,224,374,101,1,223,223,7,226,677,224,102,2,223,223,1005,224,389,101,1,223,223,8,226,677,224,1002,223,2,223,1005,224,404,101,1,223,223,1008,226,677,224,1002,223,2,223,1005,224,419,1001,223,1,223,107,677,677,224,102,2,223,223,1005,224,434,101,1,223,223,1108,677,226,224,1002,223,2,223,1006,224,449,101,1,223,223,1108,677,677,224,102,2,223,223,1006,224,464,101,1,223,223,1007,677,226,224,102,2,223,223,1006,224,479,101,1,223,223,1008,226,226,224,102,2,223,223,1006,224,494,101,1,223,223,108,226,226,224,1002,223,2,223,1006,224,509,101,1,223,223,107,226,226,224,102,2,223,223,1006,224,524,101,1,223,223,1107,677,226,224,102,2,223,223,1005,224,539,1001,223,1,223,108,226,677,224,1002,223,2,223,1005,224,554,101,1,223,223,1007,226,226,224,102,2,223,223,1005,224,569,101,1,223,223,8,226,226,224,102,2,223,223,1006,224,584,101,1,223,223,1008,677,677,224,1002,223,2,223,1005,224,599,1001,223,1,223,107,226,677,224,1002,223,2,223,1005,224,614,1001,223,1,223,1108,226,677,224,102,2,223,223,1006,224,629,101,1,223,223,7,677,677,224,1002,223,2,223,1005,224,644,1001,223,1,223,108,677,677,224,102,2,223,223,1005,224,659,101,1,223,223,1007,677,677,224,102,2,223,223,1006,224,674,101,1,223,223,4,223,99,226".split(",")]
    calculateIntcodes(my_input)
    #print(get_mode(my_input, 12))
