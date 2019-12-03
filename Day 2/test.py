import unittest
from part_1_and_2 import getInput, calculateIntcodes


class TestIntcode(unittest.TestCase):

    def test_case_1(self):
        intcodes = [1,0,0,0,99]
        calculateIntcodes(intcodes)
        self.assertEqual(intcodes,[2,0,0,0,99])

    def test_case_2(self):
        intcodes = [2,3,0,3,99]
        calculateIntcodes(intcodes)
        self.assertEqual(intcodes,[2,3,0,6,99])
    def test_case_3(self):
        intcodes = [2,4,4,5,99,0]
        calculateIntcodes(intcodes)
        self.assertEqual(intcodes,[2,4,4,5,99,9801])

    def test_case_4(self):
        intcodes = [1,1,1,4,99,5,6,0,99]
        calculateIntcodes(intcodes)
        self.assertEqual(intcodes,[30,1,1,4,2,5,6,0,99])


if __name__ == '__main__':
    unittest.main()
