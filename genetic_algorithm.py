
import random
import math
import copy 
from typing import List, Tuple

def generate_random_population(cities_location: List[Tuple[float, float]], population_size: int) -> List[List[Tuple[float, float]]]:
    """
    Generate a population of routes for a given set of cities.
    """
     # A primeira cidade é (0, 0)
    cidade_inicial = cities_location[0]  # Supondo que (0, 0) esteja na posição 0
    outras_cidades = cities_location[1:]  # Todas as outras cidades

    # Criar a população inicial
    populacao = []
    for _ in range(population_size):
        # Embaralhar as outras cidades
        ciclo = [cidade_inicial] + random.sample(outras_cidades, len(outras_cidades))
        populacao.append(ciclo)

    return populacao


def calculate_distance(point1: Tuple[float, float], point2: Tuple[float, float]) -> float:
    """
    Calculate the Euclidean distance between two points.
    """
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

def calculate_fitness(path: List[Tuple[float, float]]) -> float:
    """
    Calculate the fitness of a given path based on the total Euclidean distance.
    """
    distance = 0
    n = len(path)
    for i in range(n):
        distance += calculate_distance(path[i], path[(i + 1) % n])

    return distance

def order_crossover(parent1: List[Tuple[float, float]], parent2: List[Tuple[float, float]]) -> List[Tuple[float, float]]:
    """
    Perform order crossover (OX) between two parent sequences to create a child sequence.
    """
    length = len(parent1)

    # Choose two random indices for the crossover
    start_index = random.randint(0, length - 1)
    end_index = random.randint(start_index + 1, length)

    # Initialize the child with a copy of the substring from parent1
    child = parent1[start_index:end_index]

    # Fill in the remaining positions with genes from parent2
    remaining_positions = [i for i in range(length) if i < start_index or i >= end_index]
    remaining_genes = [gene for gene in parent2 if gene not in child]

    for position, gene in zip(remaining_positions, remaining_genes):
        child.insert(position, gene)

    return child

def mutate(solution:  List[Tuple[float, float]], mutation_probability: float) ->  List[Tuple[float, float]]:
    """
    Mutate a solution by inverting a segment of the sequence with a given mutation probability.
    """
    mutated_solution = copy.deepcopy(solution)

    # Check if mutation should occur    
    if random.random() < mutation_probability:
        
        # Ensure there are at least two cities to perform a swap
        if len(solution) < 2:
            return solution
    
        # Select a random index (excluding the last index) for swapping
        index = random.randint(0, len(solution) - 2)
        
        # Swap the cities at the selected index and the next index
        mutated_solution[index], mutated_solution[index + 1] = solution[index + 1], solution[index]   
        
    return mutated_solution

def sort_population(population: List[List[Tuple[float, float]]], fitness: List[float]) -> Tuple[List[List[Tuple[float, float]]], List[float]]:
    """
    Sort a population based on fitness values.
    """
    # Combine lists into pairs
    combined_lists = list(zip(population, fitness))

    # Sort based on the values of the fitness list
    sorted_combined_lists = sorted(combined_lists, key=lambda x: x[1])

    # Separate the sorted pairs back into individual lists
    sorted_population, sorted_fitness = zip(*sorted_combined_lists)

    return sorted_population, sorted_fitness    

