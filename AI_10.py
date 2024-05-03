# Implementation of Genetic Algorithm in Python
import random

num_of_chromosomes=6
mutation_rate=0.1
crossover_rate=0.8

def initialize_population():
    return [[random.random() for j in range(4)] for i in range(num_of_chromosomes)]

def evaluate_fitness(chromosome):
    fitness = (chromosome[0]+2*chromosome[1]+3*chromosome[2]+4*chromosome[3])-30
    return fitness

def selection(population):
    fitness_value=[evaluate_fitness(chromo) for chromo in population]
    total_fitness=sum(fitness_value)
    prob=[fitness/total_fitness for fitness in fitness_value]
    selected_indices=random.choices(range(len(population)),weights=prob,k=len(population))
    return[population[i] for i in selected_indices]

def crossover(parent1,parent2):
    crossover_points=random.randint(1,len(parent1)-1)
    child1=parent1[:crossover_points]+parent2[crossover_points:]
    child2=parent2[:crossover_points]+parent1[crossover_points:]
    return child1,child2

def mutation(chromosome):
    mutated_chromosome = chromosome[:]
    for i in range(len(mutated_chromosome)):
        if random.random() < mutation_rate:
            mutated_chromosome[i] = random.randint(0,5)
    return mutated_chromosome

population=initialize_population()
for i,chromo in enumerate(population):
    print(f"Chromosome {i} : {chromo}")

for gen in range(1000):
    evaluated_population = [(chromosome,evaluate_fitness(chromosome)) for chromosome in population]
    selected_population=selection(population)

    children=[]
    for i in range(num_of_chromosomes//2):
        parent1=random.choice(selected_population)
        parent2=random.choice(selected_population)

        child1,child2=crossover(parent1,parent2)
        children.extend([child1,child2])

    mutated_population =[mutation(chromo) for chromo in children]
    population=mutated_population

    best_chromosome=max(evaluated_population,key=lambda x:x[1])[0]
    if evaluate_fitness(best_chromosome)==0:
        print(f"No of Generations : {gen}")
        print(f"Best Chromosome : {best_chromosome}")
        break
