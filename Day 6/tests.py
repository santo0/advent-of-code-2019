import unittest
from part_1 import get_input
from part_2 import get_distance_between
def get_input():
    return open('test_input', 'r').read().split('\n')
class TestIntcode(unittest.TestCase):


    def test_case_1(self):
        my_input = get_input()
        formated_input = [tuple(orbit.split(')')) for orbit in my_input]
        dict_input = {key:(value, str_modo) for (value,key), str_modo in zip(formated_input, my_input)}
        print(get_distance_between(dict_input, 'SAN', 'YOU'))



if __name__ == '__main__':
    unittest.main()
