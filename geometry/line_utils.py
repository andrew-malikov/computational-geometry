from geometry.line import LineBuilder


def get_optimal_line(segments):
    max_points = 0
    optimal_line = None

    for i in range(0, len(segments)):
        line = LineBuilder.from_segment(segments[i])
        points = 0

        for j in range(0, len(segments)):
            if line.contain_point(segments[j].a):
                points += 1

            if line.contain_point(segments[j].b):
                points += 1

        if points >= max_points:
            max_points = points
            optimal_line = line

    return [optimal_line, max_points]
