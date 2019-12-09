from collections import namedtuple


def get_one_layer(my_input, wide_tall):
    return tuple(int(d)for d in my_input[0:wide_tall])


def get_all_layers(my_input, wide, tall):
    total_layers = list()
    for i in range(int(len(my_input)/wide*tall)):
        if len(get_one_layer(my_input[wide * tall * i:], wide * tall)) != 0:
            total_layers.append(get_one_layer(my_input[wide * tall * i:], wide * tall))
        #print(get_one_layer(my_input[wide * tall * i:], wide * tall))
    return total_layers


def get_layer_fewest_zeros(total_layers):
    zeros_of_layers = list(0 for i in range(len(total_layers)))
    some_index = 0
    for layer in total_layers:
        for c in layer:
            if c == 0:
                zeros_of_layers[some_index] += 1
        some_index += 1
    return total_layers[zeros_of_layers.index(min(zeros_of_layers))]


def get_result(layer):
    count_1 = 0
    count_2 = 0
    for c in layer:
        if c == 1:
            count_1 += 1
        elif c == 2:
            count_2 += 1
    return count_1 * count_2
