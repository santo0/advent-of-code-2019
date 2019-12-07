from collections import namedtuple
import itertools


def get_input():
    line = ""
    with open("input", "r") as f:
        line = f.readline()
    splitted = line.strip().split(",")
    intcode = [int(num)for num in splitted]
    return intcode


ThreeParam = namedtuple('ThreeParam', 'p1 p2 p3', defaults=(0,)*3)
TwoParam = namedtuple('TwoParam', 'p1 p2', defaults=(0,)*2)
OneParam = namedtuple('OneParam', 'p1', defaults=(0,))


def calculate_combinations(intcode):
    all_permutations = tuple(itertools.permutations([0, 1, 2, 3, 4]))
    cop_intcode = intcode
    total = list()
    for phase_setting in all_permutations:
        amp_output = 0
        for value in phase_setting:
            amp_output = calculate_intcodes(cop_intcode, value, amp_output)
            cop_intcode = intcode
        total.append(amp_output)
    return max(total)


def calculate_intcodes(intcode, input_1, input_2):
    second_time_input = False
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
                if not second_time_input:
                    intcode[i1] = input_1
                    second_time_input = True
                else:
                    intcode[i1] = input_2
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
                print("Bye", i0, op_code)
                return i1
          #  print("--------------------")
    except IndexError:
        print("ha petao")
        print(i0)




def get_mode(intcode, i0):
    op_code = int(str(intcode[i0])[-2:])
    op_params = str(intcode[i0])[:-2][::-1]
    if 1 == op_code or 2 == op_code or 7 == op_code or 8 == op_code:
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
    my_input = get_input()
    print(calculate_combinations(my_input))

