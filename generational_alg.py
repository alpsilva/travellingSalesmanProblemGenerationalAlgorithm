import random

from point import Point, Tour

# function to select the individuals (I chose a roulette type function)
def roulette_wheel(tours):
    # for this selection, the total distance of the tour will serve as the fitness function (we want to minimize it)
    # Start by sorting the list of routes so that the smaller ones will be first on the list
    sorted_tours = sorted(tours)
    sorted_tours_size = len(sorted_tours)

    # We will also correlate each tour with the accumulated affinity till then
    cumulative_total_distance = []
    cumulative_total_distance.append(sorted_tours[0].total_distance)

    for i in range(1, sorted_tours_size):
        cumulative_total_distance.append(sorted_tours[i].total_distance + cumulative_total_distance[i-1]) 

    # generate a random float between minimun and the maximum cumulative total distance
    random_fitness = random.uniform(cumulative_total_distance[0], cumulative_total_distance[-1])

    # now, starting from the end of the list, we select the first individual that has 
    # a smaller accumulated fitness (because we want to minimize this cost) than the random one
    selected = sorted_tours[0] # just to initialize

    # reverse the list, but enumerating it allows us to get the original index from before being reversed
    for original_index, ctd in reversed(list(enumerate(cumulative_total_distance))):
        if ctd <= random_fitness:
            selected = sorted_tours[original_index]
            return selected
    # failsafe
    return selected

def generateChild(shuffled_points, parent):
    

    crossover_chance = 75 # Chance of crossover happening
    will_crossover = False
    roll = random.randrange(100)
    if roll < crossover_chance:
        will_crossover = True

    child = None

    if (will_crossover):
        random.shuffle(shuffled_points)
        child = Tour(shuffled_points)
        # in this crossover, we determine some points on the child that will have the exact same value as the parent
        # exchanging when necessary

        # number of afflicted points
        n = random.randrange(len(parent.points))
        for N in range(n):
            # select a random point from the father
            random_index = random.randrange(len(parent.points))
            selected_point = parent.points[random_index]
            for i in range(len(child.points)):
                if child.points[i].id == selected_point.id:
                    # Exchange se we do not duplicate visits to a point
                    child.points[i] = child.points[random_index]
                    child.points[random_index] = selected_point

                    # we have to make sure the tour begins and ends on the same city
                    if (random_index == 0 or random_index == len(child.points)-1):
                        child.points[0] = selected_point
                        child.points[len(child.points)-1] = selected_point
    else:
        # child will be equal to the parent
        child = Tour(parent.points)

    # theres a small chance the child can mutate
    mutation_chance = 10 # Chance of mutation happening
    will_mutate = False
    roll = random.randrange(100)
    if roll < mutation_chance:
        will_mutate = True

    if will_mutate:
        # this mutation switchs two random points (excluding start and end points to ease implementation)
        i1 = random.randrange(1, len(child.points)-1)
        i2 = random.randrange(1, len(child.points)-1)
        aux = child.points[i1]
        child.points[i1] = child.points[i2]
        child.points[i2] = aux

    return child
    

