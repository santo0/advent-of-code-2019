import unittest
from part_2 import get_input, calculate_combinations


class TestIntcode(unittest.TestCase):
    def test_case_1(self):
        my_input = get_input('input')
        print(my_input)
        self.assertEqual(65210, calculate_combinations(my_input))

    def test_case_2(self):
        my_input = get_input('input2')
        print(my_input)
        self.assertEquals(139629729, calculate_max_thruster(my_input))

if __name__ == '__main__':
    unittest.main()
