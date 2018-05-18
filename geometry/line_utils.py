from geometry.line import LineBuilder


def get_optimal_line(points):
    max_points = []
    optimal_line = None

    points_len = len(points)
    for i in range(0, points_len - 1):
        for j in range((i + 1) % points_len, points_len):
            if points[i].is_equal(points[j]):
                continue

            line = LineBuilder.from_points(points[i], points[j])
            match_points = []

            for k in range(0, points_len):
                if line.contain_point(points[k]):
                    match_points.append(points[k])

            if len(match_points) >= len(max_points):
                max_points = match_points
                optimal_line = line

    return [max_points, optimal_line]
