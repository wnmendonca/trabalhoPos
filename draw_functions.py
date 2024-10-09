# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 16:03:11 2023

@author: SérgioPolimante
"""
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg
import matplotlib
import pygame
import numpy as np
from typing import List, Tuple


matplotlib.use("Agg")


def draw_plot(screen: pygame.Surface, x: list, y: list, x_label: str = 'Generation', y_label: str = 'Fitness') -> None:
    """
    Draw a plot on a Pygame screen using Matplotlib.

    Parameters:
    - screen (pygame.Surface): The Pygame surface to draw the plot on.
    - x (list): The x-axis values.
    - y (list): The y-axis values.
    - x_label (str): Label for the x-axis (default is 'Generation').
    - y_label (str): Label for the y-axis (default is 'Fitness').
    """
    fig, ax = plt.subplots(figsize=(4, 4), dpi=100)
    ax.plot(x, y)
    ax.set_ylabel(y_label)
    ax.set_xlabel(x_label)
    plt.tight_layout()

    canvas = FigureCanvasAgg(fig)
    canvas.draw()
    renderer = canvas.get_renderer()
    raw_data = renderer.tostring_rgb()

    size = canvas.get_width_height()
    surf = pygame.image.fromstring(raw_data, size, "RGB")
    screen.blit(surf, (0, 0))
    
def draw_cities(screen: pygame.Surface, cities_locations: List[Tuple[int, int]],city_names: List[str], rgb_color: Tuple[int, int, int], node_radius: int) -> None:
    """
    Draws circles representing cities on the given Pygame screen.

    Parameters:
    - screen (pygame.Surface): The Pygame surface on which to draw the cities.
    - cities_locations (List[Tuple[int, int]]): List of (x, y) coordinates representing the locations of cities.
    - rgb_color (Tuple[int, int, int]): Tuple of three integers (R, G, B) representing the color of the city circles.
    - node_radius (int): The radius of the city circles.

    Returns:
    None
    """
    """for city_location in cities_locations:
        pygame.draw.circle(screen, rgb_color, city_location, node_radius)"""
    
    # Configurar a fonte
    font = pygame.font.Font(None, 16)
    
    for city_location, city_name in zip(cities_locations, city_names):
        
        # Desenhar o círculo da cidade
        pygame.draw.circle(screen, rgb_color, city_location, node_radius)
        
        # Renderizar o nome da cidade
        texto_renderizado = font.render(city_name, True, (0, 0, 0))  # Cor do texto em preto
        texto_rect = texto_renderizado.get_rect(center=(city_location[0], city_location[1] - node_radius - 10))  # Posicionar acima do ponto

        # Desenhar o texto na tela
        screen.blit(texto_renderizado, texto_rect)






def draw_paths(screen: pygame.Surface, path: List[Tuple[int, int]], rgb_color: Tuple[int, int, int], width: int = 1):
    """
    Draw a path on a Pygame screen.

    Parameters:
    - screen (pygame.Surface): The Pygame surface to draw the path on.
    - path (List[Tuple[int, int]]): List of tuples representing the coordinates of the path.
    - rgb_color (Tuple[int, int, int]): RGB values for the color of the path.
    - width (int): Width of the path lines (default is 1).
    """
    pygame.draw.lines(screen, rgb_color, True, path, width=width)



