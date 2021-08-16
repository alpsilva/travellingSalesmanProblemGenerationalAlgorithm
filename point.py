import math

class Point:
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y

    def printPoint(self):
        print(self.id, self.x, self.y)

def distance(p1, p2):
    a = math.pow((p2.x - p1.x), 2)
    b = math.pow((p2.y - p1.y), 2)
    d = math.sqrt((a + b))
    return d

class Tour:
        def __init__(self, points):
            # array that stores the points route in order
            self.points = []
            # We need to make sure we are creating a new list with the same elements, and not just cloning the pointer of the list object
            for p in points:
                np = Point(p.id, p.x, p.y)
                self.points.append(np)
            total_distance = 0
            for i in range((len(points)-1)):
                d = distance(points[i], points[i+1])
                total_distance += d
            # The Tour has a closed route, so we need to account for the distance from the last point to the first
            total_distance += distance(points[-1], points[0])
            # The total distance of the tour will be used as the objective function to determine good and bad routes
            self.total_distance = total_distance

        def __lt__(self, other):
            return self.total_distance < other.total_distance
        
        def printTour(self):
            print("Route of the Tour: ")
            for point in self.points:
                print(point.id, " -> ", end = '')
            print(self.points[0].id)
            print("Total Distance: ", self.total_distance)