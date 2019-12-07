from collections import namedtuple
import itertools


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


def calculate_combinations(intcode):
    all_permutations = tuple(itertools.permutations([5, 6, 7, 8, 9]))
    intcodes_list = [[d for d in intcode] for i in range(5)]
    list_index = [0 for i in range(5)]
    total = list()
    for phase_setting in all_permutations:
        amp_output = 0
        its_time_to_stop = False
        for value in phase_setting:
            print(value, phase_setting.index(value))
            #print(intcodes_list[phase_setting.index(value)], value, amp_output, phase_setting.index(value))
            amp_output = calculate_intcodes_two_inputs(intcodes_list[phase_setting.index(value)], value, amp_output, phase_setting.index(value))
        print("---------")
        index = 0
        while not its_time_to_stop:
            amp_output, its_time_to_stop, list_index[index] = calculate_intcodes_one_input(
                intcodes_list[index], amp_output, index, list_index[index])
            print(amp_output, its_time_to_stop, list_index)
            index = (index + 1) % 5
        total.append(amp_output)
    print(max(total))


def calculate_intcodes_one_input(intcode, input_1, amp, i0):
    try:
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
                intcode[i1] = input_1
                i0 += 2
            elif op_code == 4:
                mode = get_mode(intcode, i0)
                i1 = intcode[intcode[i0 + 1]
                             ] if mode.p1 == 0 else intcode[i0 + 1]
                #print("--->op 4<---", i1, i0 + 1, amp)
                i0 += 2
                return i1, False, i0
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
                print("I am {a} and I say goodbye".format(a=amp), i0, op_code)
                if amp != 4:
                    return i1, False, i0
                else:
                    return i1, True, i0
          #  print("--------------------")
    except IndexError:
        print("ha petao")
        print(i0)


def calculate_intcodes_two_inputs(intcode, input_1, input_2, amp):
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
                print("--->op 4<---", i1, i0 + 1, amp)
                i0 += 2
                return i1
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
                print("I am {a} and I say goodbye".format(a=amp), i0, op_code)
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
    #my_input = getInput()
    my_input = [int(
        d)for d in "3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5".split(",")]
    calculate_combinations(my_input)
    #print(get_mode(my_input, 12))
