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

def generateChild(current_generation, total_generations, shuffled_points, parent1, parent2):
    
    # Chance of crossover happening
    if current_generation < total_generations / 2:
        crossover_chance = 60
    elif current_generation < total_generations / 4:
        crossover_chance = 20
    else: crossover_chance = 80
        
    will_crossover = False
    roll = random.randrange(100)
    if roll < crossover_chance:
        will_crossover = True

    child = None

    if (will_crossover):
       child = crossover(parent1, parent2)
    else:
        # child will be random
        random.shuffle(shuffled_points)
        child = Tour(shuffled_points)

    # theres a small chance the child can mutate
    mutation_chance = 20 # Chance of mutation happening
    will_mutate = False
    roll = random.randrange(100)
    if roll < mutation_chance:
        will_mutate = True

    if will_mutate:
        child = mutate(child)

    return child
    
def crossover(parent1, parent2):
    p1 = parent1.points
    p2 = parent2.points
    offspring_points = []
    p1_segment = []
    p2_segment = []
    
    # Pick a sublist of parent 1 points, and combines it with the rest of parent 2
    gene_a = int(random.random() * len(p1))
    gene_b = int(random.random() * len(p1))

    start_gene = min(gene_a, gene_b)
    end_gene = max(gene_a, gene_b)

    for i in range(start_gene, end_gene):
        p1_segment.append(p1[i])
        
    p2_segment = [item for item in p2 if item not in p1_segment]

    offspring_points = p1_segment + p2_segment
    offspring = Tour(offspring_points)
    return offspring

def mutate(individual):
    # this mutation switchs two random points (excluding start and end points to ease implementation)
    i1 = random.randrange(1, len(individual.points)-1)
    i2 = random.randrange(1, len(individual.points)-1)
    aux = individual.points[i1]
    individual.points[i1] = individual.points[i2]
    individual.points[i2] = aux
    return individual
