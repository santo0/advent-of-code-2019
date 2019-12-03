def is_this_an_intersection(rect, other_rect):
    # return is_adjacent(rect, other_rect) or is_secant(rect, other_rect)
    return is_adjacent(rect, other_rect) or is_secant(rect, other_rect)


def is_adjacent(rect, other_rect):
    for point in rect:
        if is_between(other_rect.initial_point, other_rect.final_point, point):
            return True
    return False


def is_between(point_1, point_2, point):
    if is_starting_point(point):
        return False
    elif point_1.x == point.x and point_2.x == point.x:
        return point_1.y <= point.y <= point_2.y or point_2.y <= point.y <= point_1.y
    elif point_1.y == point.y and point_2.y == point.y:
        return point_1.x <= point.x <= point_2.x or point_2.x <= point.x <= point_1.x
    else:
        False


def is_starting_point(point):
    return point.x == 0 and point.y == 0


def is_secant(rect, other_rect):
    # O es horitzontal
    if rect.initial_point.x == rect.final_point.x:
        if other_rect.initial_point.x == other_rect.final_point.x:
            return
        else:
            return
    # O es vertical
    else:
        if other_rect.initial_point.x == other_rect.final_point.x:
            comm_point = Point(other_rect.initial_point.x,
                               rect.initial_point.y)
            return (rect.initial_point.x <= comm_point.x <= rect.final_point.x
                    and rect.initial_point.y <= comm_point.y <= rect.final_point.y) \
                or (rect.final_point.x <= comm_point.x <= rect.initial_point.x
                    and rect.final_point.y <= comm_point.y <= rect.initial_point.y)
        else:
            comm_point = Point(other_rect.initial_point.x,
                               rect.initial_point.y)
            return (rect.initial_point.x <= comm_point.x <= rect.final_point.x
                    and rect.initial_point.y <= comm_point.y <= rect.final_point.y) \
                or (rect.final_point.x <= comm_point.x <= rect.initial_point.x
                    and rect.final_point.y <= comm_point.y <= rect.initial_point.y)
