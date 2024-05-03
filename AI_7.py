# Implementation of Hill Climbing in Python
import random

def objective_func(x):
    return -x**2

def generate_initial_soln():
    return random.randint(-100,100)

def generate_neighbours(soln):
    neighbours=[]
    for i in [-1,1]:
        neighbours.append(soln+i)
    return neighbours

def generate_best_neighbour(neighbours):
    best_neighbour=neighbours[0]
    best_quality=objective_func(best_neighbour)
    for neighbour in neighbours[1:]:
        neighbour_quality=objective_func(neighbour)
        if neighbour_quality>best_quality:
            best_quality=neighbour_quality
            best_neighbour=neighbour
    return best_neighbour

def hill_climb():
    curr_soln=generate_initial_soln()
    print(f"Initial solution is : {curr_soln}")
    while True:
        neighbours=generate_neighbours(curr_soln)
        best_neighbours=generate_best_neighbour(neighbours)
        if objective_func(best_neighbours)<=objective_func(curr_soln):
            return curr_soln
        curr_soln=best_neighbours

best_soln=hill_climb()
print(f"Best Solution Found at {best_soln}")
print(f"Objective Value of the best solution is : {objective_func(best_soln)}")
