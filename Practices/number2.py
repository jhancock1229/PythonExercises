class Point:
    """
    A class implementation of 2-Dimensional point.
    """


    def __init__(self, x, y):
        self.x = x
        self.y = y


    def __add__(self, other):
        return Point(self.x+other.x, self.y+other.y)

    def __sub__(self, other):
        return Point(self.x-other.x, self.y-other.y)

    def __str__(self):
        return '(%d, %d)' % (self.x, self.y)



p1 = Point(8, 5)
p2 = Point(-6, 1)

print p1 + p2
print p1 - p2