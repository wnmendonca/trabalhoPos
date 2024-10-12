# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 16:03:11 2023

@author: SérgioPolimante
"""
import matplotlib.pyplot as plt
import streamlit as st
import matplotlib


matplotlib.use("Agg")

def draw_plot(cities_locations, city_names, path, best_path, title):
    plt.clf()  # Limpa a figura anterior para evitar sobreposição
    
    for city_location, city_name in zip(cities_locations, city_names):
        plt.scatter(city_location[0], city_location[1], color='green', s=100)
        plt.text(city_location[0] + 0.1, city_location[1], city_name, fontsize=9)
    
    # Plotar o caminho atual
    x_current = [tree[0] for tree in path]
    y_current = [tree[1] for tree in path]
    plt.plot(x_current, y_current, 'b--', label='Caminho Atual')

    # Plotar o melhor caminho
    x_best = [tree[0] for tree in best_path]
    y_best = [tree[1] for tree in best_path]
    plt.plot(x_best, y_best, 'r-', linewidth=1, label='Melhor Caminho')

    plt.xlabel('Coordenada X')
    plt.ylabel('Coordenada Y')
    plt.title(title)
    plt.legend()

    # Retorna a figura gerada
    st.pyplot(plt.gcf())