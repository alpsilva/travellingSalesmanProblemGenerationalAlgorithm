#%%
import random
import matplotlib.pyplot as plt
import numpy as np

from input import populate_points_array
from point import Tour
from generational_alg import roulette_wheel, generateChild

# array of points read from the points.txt file
points = populate_points_array()

# Another array that we will be shuffling a lot (I made a copy se we don't lose the original :D)
shuffled_points = []
for point in points:
    shuffled_points.append(point)

# Defines how many generations the algorithm will produce before stopping
num_generations = 100
# Defines how many individuals each generation will have
num_individuals_per_generation = 100

# array that will be used to plot graphics
tops = []

# Current population
population = []
# Initializing population at random
for p in range (num_individuals_per_generation):
    random.shuffle(shuffled_points)
    new_random_tour = Tour(shuffled_points)
    population.append(new_random_tour)

print("Initiating generation: ")
for g in range(num_generations):
    print(g, " ", end='')

    sorted_population = sorted(population)

    top_5_avg = 0
    for i in range(5):
        top_5_avg += sorted_population[i].total_distance
    top_5_avg = top_5_avg / 5

    tops.append(top_5_avg)

    # Selecting a parcel of the individuals that will be used to produce the next generation
    num_parents = num_individuals_per_generation/10
    parents = []
    for i in range(num_parents):
        selected = roulette_wheel(population)
        # remove the selected individual from the general population and adds it to the parent pool
        population.remove(selected)
        parents.append(selected)
    
    population = []
    for p in range (num_individuals_per_generation):
        parent_index = random.randrange(num_parents)
        parent = parents[parent_index]
        child = generateChild(shuffled_points, parent)
        population.append(child)
# %%

#%%
print("")
# The generations have developed and we should be left with some individuals that are generally better at the problem
# So now we order the population by the smallest tota_distance and print the top 5 candidates
sorted_population = sorted(population)
print("Top #1: ")
sorted_population[0].printTour()
print("Top #2: ")
sorted_population[1].printTour()
print("Top #3: ")
sorted_population[2].printTour()
print("Top #4: ")
sorted_population[3].printTour()
print("Top #5: ")
sorted_population[4].printTour()

avg = 0
for tour in sorted_population:
    avg += tour.total_distance
avg = avg / len(sorted_population)
print("Average total distance of the last generation: ", avg)

plt.stem(np.arange(0, num_generations, 1), tops)

plt.legend('Average top 5 distances in all generations')
plt.show()
# %%
