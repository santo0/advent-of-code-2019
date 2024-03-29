import unittest
from part_1 import calculate_closest_intersection_distance


class TestIntcode(unittest.TestCase):

    def test_case_1(self):
        wires = ('R8,U5,L5,D3', 'U7,R6,D4,L4')
        intersection_distance = calculate_closest_intersection_distance(wires)
        self.assertEqual(intersection_distance, 6)

    def test_case_2(self):
        wires = ('R75,D30,R83,U83,L12,D49,R71,U7,L72',
                 'U62,R66,U55,R34,D71,R55,D58,R83')
        intersection_distance = calculate_closest_intersection_distance(wires)
        self.assertEqual(intersection_distance, 159)

    def test_case_3(self):
        wires = ('R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51',
                 'U98,R91,D20,R16,D67,R40,U7,R15,U6,R7')
        intersection_distance = calculate_closest_intersection_distance(wires)
        self.assertEqual(intersection_distance, 135)


if __name__ == '__main__':
    unittest.main()
