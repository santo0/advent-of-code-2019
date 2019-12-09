import unittest
from part_2 import get_input, calculate_combinations, calculate_max_thruster


class TestIntcode(unittest.TestCase):
    def test_case_1(self):
        my_input = get_input('input')
        self.assertEqual(17406, calculate_combinations(my_input))

    def test_case_2(self):
        my_input = get_input('input2')
        calculate_max_thruster(my_input)
        #self.assertEquals(139629729, calculate_max_thruster(my_input))

if __name__ == '__main__':
    unittest.main()
