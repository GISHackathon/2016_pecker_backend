from math import radians, cos, sin, asin, sqrt


class PointBuffer(object):
    def __init__(self, point, radius):
        self.center = point
        self.radius = radius

    def is_point_within(self, point):
        print self.get_distance(point)
        if self.get_distance(point) < self.radius:
            return True
        else:
            return False

    def get_distance(self, point):
        c_x_rad = radians(self.center.x_coord)
        c_y_rad = radians(self.center.y_coord)
        p_x_rad = radians(point.x_coord)
        p_y_rad = radians(point.y_coord)

        dlon = p_x_rad - c_x_rad
        dlat = p_y_rad - c_y_rad
        a = sin(dlat / 2) ** 2 + cos(c_y_rad) * cos(p_y_rad) * sin(dlon / 2) ** 2
        c = 2 * asin(sqrt(a))
        r = 6371
        return c * r
