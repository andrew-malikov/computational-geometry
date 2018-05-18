from math import hypot
from operator import methodcaller


def jarvis_algorithm(points: list):
    return sorted(iter(points), key=methodcaller('get_arc'))


def left_most_point(pts):
    if not isinstance(pts, list):
        return False
    curr = pts[0]
    for pt in pts[1:]:
        if pt.x < curr.x or (pt.x == curr.x and pt.y < curr.y):
            curr = pt
    return curr


def cross_product(p, p1, p2):
    return (p.y - p2.y) * (p.x - p1.x) - (p.y - p1.y) * (p.x - p2.x)


def distance(p, p1, p2):
    return hypot(p.x - p1.x, p.y - p1.y) - hypot(p.x - p2.x, p.y - p2.y)


def iter(pts):
    colinear = list()
    curr_pt = left_most_point(pts)
    convex_list = [curr_pt]

    for pt1 in pts:
        if curr_pt.is_equal(pt1):
            continue
        target = pt1
        for pt2 in pts:
            if pt2.is_equal(target) or pt2.is_equal(curr_pt):
                continue

            res = cross_product(curr_pt, target, pt2)
            if res > 0:
                colinear = list()
                target = pt2
            elif res == 0:
                if distance(curr_pt, target, pt2) > 0:
                    if pt2 not in colinear:
                        colinear.append(pt2)
                else:
                    if target not in colinear:
                        colinear.append(target)
                    target = pt2

        if target not in convex_list:
            convex_list.append(target)

        for colinear_pt in colinear:
            if colinear_pt not in convex_list:
                convex_list.append(colinear_pt)

        curr_pt = target
    return convex_list
