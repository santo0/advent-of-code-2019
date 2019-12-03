from collections import namedtuple


class Rect:
    def __init__(self, p0, p1):
        self.p0 = p0
        self.p1 = p1

    def is_vertical(self):
        return self.p0.x == self.p1.x

    def is_horizontal(self):
        return self.p0.y == self.p1.y

    def is_in_vertical(self, other):
        return (self.p0.y <= other.p0.y <= self.p1.y
                or self.p1.y <= other.p0.y <= self.p0.y)\
            and (other.p0.x <= self.p0.x <= other.p1.x
                 or other.p1.x <= self.p0.x <= other.p0.x)

    def is_in_horizontal(self, other):
        return (self.p0.x <= other.p1.x <= self.p1.x
                or self.p1.x <= other.p1.x <= self.p0.x)\
            and (other.p0.y <= self.p1.y <= other.p1.y
                 or other.p1.y <= self.p1.y <= other.p0.y)

    def calculate_intersection_h_v(self, other):
        if other.p1.x == 0 and self.p1.y == 0:
            return None
        else:
            return Point(other.p1.x, self.p1.y)

    def calculate_intersection_v_h(self, other):
        if self.p1.x == 0 and other.p1.y == 0:
            return None
        else:
            return Point(self.p1.x, other.p1.y)

    def __str__(self):
        return 'Rect({p_1},{p_0})'.format(p_1=self.p1, p_0=self.p0)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return 'Point(X={x},Y={y})'.format(x=self.x, y=self.y)


STARTING_POINT = Point(0, 0)
DIRECTIONS = {"U": Point(0, 1), "D": Point(
    0, -1), "L": Point(-1, 0), "R": Point(1, 0)}


def get_input():
    with open('input', 'r') as f:
        return tuple(line for line in f)


def calculate_closest_intersection_distance(wires):
    paths = tuple(calculate_path_as_vectors(wire) for wire in wires)
    intersections = list()
    slicer = 1
    for path in paths:
        for other_path in paths[slicer:]:
            intersections.append(get_intersections(path, other_path))
            slicer += 1
    print(intersections)
# toque a 3,3 i 6,5


def get_intersection_point(rect, other_rect):
    if rect.is_vertical() and rect.is_in_vertical(other_rect):
        if other_rect.is_vertical():
            print("pls god no")
            return None
        elif other_rect.is_horizontal():
            return rect.calculate_intersection_v_h(other_rect)
        else:
            return None
    elif rect.is_horizontal() and rect.is_in_horizontal(other_rect):
        if rect.p1.x == 3 and rect.p0.x == 3 or rect.p0.x == 8 and rect.p1.x == 3:
            print("e")
        if other_rect.is_vertical():
            return rect.calculate_intersection_h_v(other_rect)
        elif other_rect.is_horizontal():
            return None
            print("nope")
        else:
            return None
    else:
        return None
def calculate_distance_manhattan(point):
    return abs(point.x - STARTING_POINT.x) + abs(point.y - STARTING_POINT.y)


def get_intersections(path, other_path):
    distance = list()
    first_point = path[0]
    for last_point in path[1:]:
        rect = Rect(first_point, last_point)
        first_point = last_point
        other_first_point = other_path[0]
        for other_last_point in other_path[1:]:
            other_rect = Rect(other_first_point, other_last_point)
            intersection = get_intersection_point(rect, other_rect)
            if intersection != None:
                print(intersection)
                print(rect, other_rect)
                distance.append(calculate_distance_manhattan(intersection))
            other_first_point = other_last_point
    return distance


def calculate_path_as_vectors(wire):
    splitted = wire.split(',')
    print(len(splitted))
    path = list()
    path.append(STARTING_POINT)
    last_point = STARTING_POINT
    for mov in splitted:
        new_point = get_rect(mov, last_point)
        path.append(new_point)
        last_point = new_point
    return path


def get_rect(mov, last_point):
    direction = DIRECTIONS[mov[0]]
    distance = int(mov[1:])
    new_point = Point(direction.x*distance + last_point.x,
                      direction.y*distance + last_point.y)
    return new_point


if __name__ == '__main__':
    wires = get_input()
    #wires = ('R8,U5,L5,D3', 'U7,R6,D4,L4')
    calculate_closest_intersection_distance(wires)
