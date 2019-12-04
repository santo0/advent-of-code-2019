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
        return 'Rect(p1={p_1},p0={p_0})'.format(p_1=self.p1, p_0=self.p0)

    def __sub__(self, other):
        return Rect(Point(self.p1.x-other.p1.x, self.p1.y-other.p1.y), Point(self.p0.x-other.p0.x, self.p0.y-other.p0.y))


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
            intersections.append(calculate_distance_manhattan(inter)
                                 for inter in get_intersections(path, other_path))
            slicer += 1
    return min(intersections[0])


def get_all_intersections(wires):
    paths = tuple(calculate_path_as_vectors(wire) for wire in wires)
    intersections = list()
    slicer = 1
    for path in paths:
        for other_path in paths[slicer:]:
            intersections.append(get_optimal_intersection(path, other_path))
            slicer += 1
    return intersections[0]


# No conto els solapats
def get_intersection_point(rect, other_rect):
    if rect.is_vertical() and rect.is_in_vertical(other_rect):
        if other_rect.is_vertical():
            return None
        elif other_rect.is_horizontal():
            return rect.calculate_intersection_v_h(other_rect)
        else:
            return None
    elif rect.is_horizontal() and rect.is_in_horizontal(other_rect):
        if other_rect.is_vertical():
            return rect.calculate_intersection_h_v(other_rect)
        elif other_rect.is_horizontal():
            return None
        else:
            return None
    else:
        return None


def calculate_distance_manhattan(point):
    return abs(point.x - STARTING_POINT.x) + abs(point.y - STARTING_POINT.y)


def calculate_manhattan(point_1, point_0):
    return abs(point_1.x - point_0.x) + abs(point_1.y - point_0.y)


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
                distance.append(intersection)
            other_first_point = other_last_point
    return distance


def get_optimal_intersection(path, other_path):
    distance = list()
    first_point = path[0]
    total_steps = list()
    path_steps = 0
    other_path_steps = 0
    for last_point in path[1:]:
        rect = Rect(first_point, last_point)
        other_first_point = other_path[0]
        path_steps = path_steps + calculate_manhattan(last_point, first_point)
        for other_last_point in other_path[1:]:
            other_rect = Rect(other_first_point, other_last_point)
            intersection = get_intersection_point(rect, other_rect)
            other_path_steps += calculate_manhattan(
                other_last_point, other_first_point)
            if intersection != None:
                #
                #
                #
                diff_steps = abs(intersection.x - rect.p1.x) + abs(intersection.y - rect.p1.y)
                diff_other_steps = abs(intersection.x - other_rect.p1.x) + abs(intersection.y - other_rect.p1.y)
                distance.append(intersection)
                total_steps.append(path_steps - diff_steps + other_path_steps - diff_other_steps)
                #
                #
                #
                #
            other_first_point = other_last_point
        other_path_steps = 0
        first_point = last_point
    return total_steps


def calculate_path_as_vectors(wire):
    splitted = wire.split(',')
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
    distance = calculate_closest_intersection_distance(wires)
    all_intersections = get_all_intersections(wires)
    print(min(all_intersections))