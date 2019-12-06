def get_input():
    return open('input', 'r').read().split('\n')


def is_wanted_space_object(orbit, wanted_space_object):
    return orbit[0:3] == wanted_space_object, orbit


def get_sum_of_orbits(my_input):
    total = 0
    for orbit in my_input:
        total += get_orbits(my_input, orbit)   
    return total     

def get_orbits_recur(my_input, obj):
    orbiting_to = my_input[obj]
    if not orbiting_to:
        return 0
    else:
        return get_orbits_recur(my_input, obj) + 1

def get_orbits(my_input, obj):
    orbiting_to = my_input[obj]
    total = 0
    try:
        while 1:
            total += 1
            orbiting_to = my_input[orbiting_to]
    except KeyError:
        return total

if __name__ == '__main__':
    my_input = get_input()
    formated_input = [tuple(orbit.split(')')) for orbit in my_input]
    dict_input = {key:value for (value,key) in formated_input}
    print(get_sum_of_orbits(dict_input))
