# -*- coding: utf-8 -*-

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
    
def draw_cities(screen: pygame.Surface, cities_locations: List[Tuple[int, int]],city_names: List[str], node_radius: int) -> None:
    """
    Draws circles representing cities on the given Pygame screen.
    """

    # Configurar a fonte
    font = pygame.font.Font(None, 16)
    
    for city_location, city_name in zip(cities_locations, city_names):
        
        # Desenhar a árvore 
        draw_tree(screen, city_location[0], city_location[1])
        
        # Renderizar o nome da cidade
        texto_renderizado = font.render(city_name, True, (0, 0, 0))  # Cor do texto em preto
        texto_rect = texto_renderizado.get_rect(center=(city_location[0], city_location[1] - node_radius - 10))  # Posicionar acima do ponto

        # Desenhar o texto na tela
        screen.blit(texto_renderizado, texto_rect)

def draw_tree(screen, x, y):
    # Definir dimensões para o tronco e a copa da árvore
    trunk_width = 6   # Largura do tronco 
    trunk_height = 12  # Altura do tronco 
    BROWN = (139, 69, 19)
    GREEN = (34, 139, 34)
    
    # Desenhar o tronco da árvore (retângulo)
    pygame.draw.rect(screen, BROWN, (x - trunk_width // 2, y, trunk_width, trunk_height))

    # Desenhar a copa da árvore (círculos)
    pygame.draw.circle(screen, GREEN, (x, y - 8), 10)  # Círculo maior da copa 
    pygame.draw.circle(screen, GREEN, (x - 10, y - 12), 7)  # Círculo esquerdo 
    pygame.draw.circle(screen, GREEN, (x + 10, y - 12), 7)  # Círculo direito 

def draw_paths(screen: pygame.Surface, path: List[Tuple[int, int]], rgb_color: Tuple[int, int, int], width: int = 1):
    """
    Draw a path on a Pygame screen.
    """
    #pygame.draw.lines(screen, rgb_color, True, path, width=width)

    font = pygame.font.Font(None, 24)  # Define a font for numbering the path

    # Desenhar as linhas que conectam os pontos (cidades)
    pygame.draw.lines(screen, rgb_color, True, path, width=width)

    # Para cada ponto do caminho, desenhar o número correspondente
    for i in range(len(path)):
        next_i = (i + 1) % len(path)  # Para conectar o último ao primeiro
        midpoint = (
            (path[i][0] + path[next_i][0]) // 2,
            (path[i][1] + path[next_i][1]) // 2,
        )

        # Ajustar a posição para deslocar o número um pouco para cima da linha
        number_position = (midpoint[0], midpoint[1] - 10)  # Deslocar 10 pixels para cima

        # Renderizar o número próximo à linha
        number_surface = font.render(str(i + 1), True, (255, 0, 0))  # Números em vermelho
        number_rect = number_surface.get_rect(center=number_position)
        screen.blit(number_surface, number_rect)



