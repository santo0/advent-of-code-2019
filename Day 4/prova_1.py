my_input = '273025-767253'
A, B = my_input.split('-')
list_of_valids = list()


def check_if_valid(code):
    no_decrease = True
    repeated = False
    last_d = code[0]
    for d in code[1:]:
        if int(last_d) > int(d):
            no_decrease = False
        if int(last_d) == int(d):
            repeated = True
        last_d = d
    return no_decrease, repeated


def check_if_valid_part_2(code):
    no_decrease = True
    repeated = False
    matching_digits_group = False
    same_digit_counter = 0
    same_digit_list = list()
    last_d = code[0]
    for d in code[1:]:
        if int(last_d) > int(d):
            no_decrease = False
        if not matching_digits_group:
            if int(last_d) == int(d):
                #repeated = True
                matching_digits_group = True
                same_digit_counter += 2
        else:
            if int(last_d) != int(d):
                matching_digits_group = False
                same_digit_list.append(same_digit_counter)
                same_digit_counter = 0
            else:
                same_digit_counter += 1
                #repeated = False
        last_d = d
    same_digit_list.append(same_digit_counter)
    if 2 in same_digit_list:
        non_group = True
    else:
        non_group = False

    return no_decrease, non_group


for code in range(int(A), int(B)):
    no_decrease, non_group = check_if_valid_part_2(str(code))
    if no_decrease and non_group:
        list_of_valids.append(code)

print(check_if_valid_part_2(str(112233)))
print(check_if_valid_part_2(str(123444)))
print(check_if_valid_part_2(str(111122)))
print(len(list_of_valids))
