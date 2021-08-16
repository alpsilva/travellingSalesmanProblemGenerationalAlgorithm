from point import Point

def populate_points_array():
    # Array that will store the points
    points = []

    # Reading from points.txt
    lines = []
    file = open('data/points.txt', 'r')
    lines = file.readlines()
    file.close()

    # Iterating over every line of points.txt
    for line in lines:
        # spliting the line into values and creating a new point
        words = line.split()
        id_input = int(words[0])
        x_input = float(words[1])
        y_input = float(words[2])
        p = Point(id_input, x_input, y_input)
        points.append(p)

    return points