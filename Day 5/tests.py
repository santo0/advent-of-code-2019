import unittest
import part_2
def get_input(f_name):
    f = open(f_name,'r')
    line = f.read()
    f.close()
    splitted = line.strip().split(",")
    intcode = [int(num)for num in splitted]
    return intcode

class TestIntcode(unittest.TestCase):
    def test_case_1(self):
        my_input = get_input('input1')
        Machina = part_2.Computer(my_input)
        Machina.set_input(8)
        self.assertEqual(1000, Machina.process_code_sequence())
    
    def test_case_2(self):
        my_input = get_input('input2')
        Machina = part_2.Computer(my_input)
        Machina.set_input(5)
        self.assertEqual(7161591, Machina.process_code_sequence())

    def test_case_3(self):
        my_input = get_input('input2')
        Machina = part_2.Computer(my_input)
        Machina.set_input(1)
        self.assertEqual(5577461, Machina.process_code_sequence())



if __name__ == '__main__':
    unittest.main()
