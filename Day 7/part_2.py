from collections import namedtuple
import itertools
from machine import calculate_intcodes, calculate_intcodes_1, calculate_intcodes_2


def get_input(f_name):
    line = ""
    with open(f_name, "r") as f:
        line = f.readline()
    splitted = line.strip().split(",")
    intcode = [int(num)for num in splitted]
    return intcode


def calculate_combinations(intcode):
    all_permutations = tuple(itertools.permutations([i for i in range(5)]))
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
    all_permutations = tuple(itertools.permutations([i for i in range(5, 10)]))
    # Each list inside this list represents the amps
    total = list()
    for perm in all_permutations:
        intcodes_list = [[d for d in intcode] for i in range(5)]
        index_list = [0 for i in range(5)]
        index = 0
        amp_signal = 0
        for amp in intcodes_list:
            # Changes the states of the amp and returns the position where it paused
            amp_signal, new_index = calculate_intcodes_1(
                amp, index_list[index], perm[index], amp_signal)
            index_list[index] = new_index
            index = (index + 1) % 5
        finished_list = [False for i in range(5)]
        while finished_list[4] == False:
            if finished_list[index] == False:
                amp_signal, new_index, new_finish = calculate_intcodes_2(
                    amp, index_list[index], amp_signal)
                index_list[index] = new_index
                finished_list[index] = new_finish
            index = (index + 1) % 5
        total.append(amp_signal)
        print(index_list)
    print(max(total))
    return max(total)


if __name__ == '__main__':
    my_input = get_input('input')
    print(calculate_combinations(my_input))
