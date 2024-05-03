# Crossover function of Genetic Algorithm in Python
import random

num_chromosomes=6
crossover_rate=0.25

def initialize_population():
    return [[random.randint(0,5) for j in range(4)] for i in range(num_chromosomes)]

def binary(population):
    return {key :[bin(gene)[2:] for gene in value] for key,value in population.items()}

def crossover(parents):
    keys = list(parents.keys())
    for i in range(len(keys)):
        idx1, idx2 = keys[i], keys[(i + 1) % len(keys)]
        crossover_point = random.randint(1, len(parents[idx1]) - 1)
        parents[idx1] = parents[idx1][:crossover_point] + parents[idx2][crossover_point:]

def crossover_select(population):
    rates=[random.random() for i in range(len(population))]
    print(f"The Rates of Chromosomes are : ")
    print(rates)
    parents = {i: chrom for i, chrom in enumerate(population) if rates[i] < crossover_rate}
    print(f"Chromosomes before population")
    print(parents)
    print(f"Binary Chromosomes before population")
    print(binary(parents))

    crossover(parents)

    print(f"Chromosomes after population")
    print(parents)
    print(f"Binary Chromosomes after population")
    print(binary(parents))

population=initialize_population()
print("Initial Population : ")
for i, chromo in enumerate(population):
    print(f"Chromosome {i+1} : {chromo}")
crossover_select(population)
