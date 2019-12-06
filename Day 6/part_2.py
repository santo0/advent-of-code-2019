def get_input():
    return open('input', 'r').read().split('\n')


def is_wanted_space_object(orbit, wanted_space_object):
    return orbit[0:3] == wanted_space_object, orbit


def get_distance_between(my_input, obj1, obj2):
       l1 = get_orbits(my_input, obj1)
       l2 = get_orbits(my_input, obj2)
       return triangulate_distance(l1, l2) - 2


def get_orbits(my_input, obj):
    orbiting_to = my_input[obj]
    list_of_orbits = list()
    try:
        while 1:
            list_of_orbits.append(orbiting_to[1])
            orbiting_to = my_input[orbiting_to[0]]
    except KeyError:
        return list_of_orbits


def triangulate_distance(l1, l2):
    distance = 0
    for obj1 in l1:
        if obj1 in l2:
            distance += l1.index(obj1)
            break
    for obj2 in l2:
        if obj2 in l1:
            distance += l2.index(obj2)
            break
    return distance
    
if __name__ == '__main__':
    my_input = get_input()
    formated_input = [tuple(orbit.split(')')) for orbit in my_input]
    dict_input = {key:(value, str_modo) for (value,key), str_modo in zip(formated_input, my_input)}
    print(get_distance_between(dict_input, 'YOU', 'SAN'))
    #print(dict_input)
