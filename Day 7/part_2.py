from collections import namedtuple
import itertools
from machine import calculate_intcodes

def get_input(f_name):
    line = ""
    with open(f_name, "r") as f:
        line = f.readline()
    splitted = line.strip().split(",")
    intcode = [int(num)for num in splitted]
    return intcode

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

def calculate_max_thruster(intcode):
    all_permutations = tuple(itertools.permutations([0, 1, 2, 3, 4]))
    intcodes_list = [[d for d in intcode] for i in range(5)]
    total = list()


    return max(total)
 




if __name__ == '__main__':
    my_input = get_input('input')
    print(calculate_combinations(my_input))
