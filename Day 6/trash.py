from anytree import Node, RenderTree
import re

def get_input():
    return open('input','r').read().split('\n')



def found_orbits(my_input, space_object_node):
    at_least_one_orbiting = False
    found_orbits_nodes = list()
    for orbit in my_input:
        found_orbit=is_wanted_space_object(orbit, space_object_node.name)
        if found_orbit:
            found_orbits_nodes.append(Node(found_orbit, space_object_node))
            at_least_one_orbiting = True
    if not at_least_one_orbiting:
        return None
    else:
        for orbit_node in found_orbits_nodes:
            found_orbits(input, orbit_node)
            


def is_wanted_space_object(orbit, wanted_space_object):
    is_in_orbit = orbit[0:3] == wanted_space_object
    if is_in_orbit:
        return orbit
    else:
        return None

def get_sum_of_orbits(my_input):
    com = Node('com')
    found_orbits(my_input, com)
        
    return 2


if __name__ == '__main__':
    my_input = get_input()
    get_sum_of_orbits(my_input)