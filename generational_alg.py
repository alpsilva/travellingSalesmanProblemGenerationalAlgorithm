import random

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
        print(original_index, ctd)
        if ctd <= random_fitness:
            selected = sorted_tours[original_index]
            return selected
    # failsafe
    return selected

