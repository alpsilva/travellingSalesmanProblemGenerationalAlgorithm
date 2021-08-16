import math

class Point:
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y

def distance(p1, p2):
    d = math.sqrt(((p2.x - p1.x)^2) + ((p2.y - p1.y)^2))
    return d