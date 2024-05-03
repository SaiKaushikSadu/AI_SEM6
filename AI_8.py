# Mutation in Genetic with Binary
import random

num_chromosomes=6
mutation_rate=0.1

def initialize_population():
    return [[random.randint(0,5) for j in range(4)] for i in range(num_chromosomes)]

def binary(population):
    return [[bin(gene)[2:] for gene in chromosome] for chromosome in population]

def mutation(population):
    mutated_population=[[random.randint(0,5) if random.random()<mutation_rate else gene for gene in chromosome] for chromosome in population]
    print(f"Mutated population : \n{mutated_population}")
    print(f"Mutated binary population : \n{binary(mutated_population)}")

population=initialize_population()
print(f"Initial Population is : \n{population}")
print(f"Initial Binary Population is : \n{binary(population)}")

mutation(population)