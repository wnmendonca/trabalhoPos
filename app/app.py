import streamlit as st
import random
import itertools
from genetic_algorithm import mutate, order_crossover, generate_random_population, calculate_fitness, sort_population
from draw_functions import draw_plot
import sys
import numpy as np
from dados import *
import time
import pandas as pd

def convert_object_list(object_list):
    names = []
    locations = []
    
    for obj in object_list:
        names.append(obj['name'])
        locations.append((obj['x'], obj['y']))
    
    return names, locations

# Define constant values
NODE_RADIUS = 10
FPS = 30
PLOT_X_OFFSET = 450

# GA
POPULATION_SIZE = 45
N_GENERATIONS = None

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

WIDTH, HEIGHT = 1500, 900

trees_list = np.array(trees)
city_names, cities_locations = convert_object_list(trees_list)
max_x = max(point[0] for point in cities_locations)
max_y = max(point[1] for point in cities_locations)
scale_x = (WIDTH - PLOT_X_OFFSET - NODE_RADIUS) / max_x
scale_y = HEIGHT / max_y
cities_locations = [(int(point[0] * scale_x + PLOT_X_OFFSET),
                     int(point[1] * scale_y)) for point in cities_locations]

# ----- Using dados

# Initialize session state
if 'generation_counter' not in st.session_state:
    st.session_state.generation_counter = itertools.count(start=1)
    st.session_state.start_sim = False

# Initialize
st.title("Tech Challenge - Algoritmos Genéticos")
st.divider()
st.markdown('''
            **Grupo 1:**
            - Celeste Magela: - rm357815
            - Rafael Ornelas - rm357804
            - Rander Rodrigues - rm357802
            - Willian Diniz - rm357814
            - Willian Mendonça - rm357832
            
            **Introdução**

            Diante do desafio de escolher um problema real e resolver utilizando Algoritmos genéticos.
            O grupo trouxe a proposta de resolver a irrigação de um pomar em um sítio com o menor percurso.''')

st.divider()

st.title("Dados")
df = pd.DataFrame(trees)
st.dataframe(df)

st.divider()

st.title("Resultado da Simulação")

# Sidebar for interaction
mutation_probability = st.slider("Probabilidade de Mutação", 0, 100, 10, 1)
apply_elitism = st.checkbox("Aplicar Elitismo")

# Create Initial Population
population = generate_random_population(cities_locations, POPULATION_SIZE)
best_fitness_values = []
best_solutions = []

# Main game loop
if st.button("Executar Simulação") or st.session_state.start_sim == True:
    st.session_state.start_sim = True
    
    plot_placeholder = st.empty()

    while st.session_state.start_sim:
        generation = next(st.session_state.generation_counter)
        
        population_fitness = [calculate_fitness(
            individual) for individual in population]

        population, population_fitness = sort_population(
            population,  population_fitness)

        best_fitness = calculate_fitness(population[0])
        best_solution = population[0]

        best_fitness_values.append(best_fitness)
        best_solutions.append(best_solution)

        with plot_placeholder:
            draw_plot(cities_locations, city_names, population[1], best_solution, f'Geração {generation}')

        print(f"Generation {generation}: Best fitness = {round(best_fitness, 2)}")

        new_population = [population[0]]  # Keep the best individual: ELITISM

        while len(new_population) < POPULATION_SIZE:
            probability = 1 / np.array(population_fitness)
            parent1, parent2 = random.choices(population, weights=probability, k=2)
            child1 = order_crossover(parent1, parent1)
            child1 = mutate(child1, mutation_probability)
            new_population.append(child1)

        population = new_population

    time.sleep(0.5)  # Simulate delay
