import unittest
import part_1
import part_2


def get_input(f_name):
    f = open(f_name, 'r')
    line = f.read()
    f.close()
    return line


class TestIntcode(unittest.TestCase):
    def test_case_1(self):
        my_input = get_input('input')
        layers = part_1.get_all_layers(my_input, 25, 6)
        layer_fewest_zeros = part_1.get_layer_fewest_zeros(layers)
        self.assertEqual(2080, part_1.get_result(layer_fewest_zeros))

    def test_case_2(self):
        my_input = get_input('input')
        layers = part_1.get_all_layers(my_input, 25, 6)
        transposed_pixels = part_2.get_transposing_pixels(layers, 25, 6)
        part_2.get_result(transposed_pixels, 25, 6)
    def test_case_3(self):
        my_input = get_input('input2')
        layers = part_1.get_all_layers(my_input, 2, 2)
        transposed_pixels = part_2.get_transposing_pixels(layers, 2, 2)
        part_2.get_result(transposed_pixels, 2, 2)


if __name__ == '__main__':
    unittest.main()
