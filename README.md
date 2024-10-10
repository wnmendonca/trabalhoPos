#  Problema de irrigação de plantas usando algoritmo Genético

Este repositório contém uma implementação Python de um solucionador de irrigação de jardim usando um algoritmo genético (GA) com base no Caixeiro Viajante.
Usamos como parametro o algoritmo apresentado em aula pelo professor com alguns ajustes

- Alteramos a função generate_random_population para iniciar sempre do ponto 0
- Alteramos a função draw_cities para renderizar um desenho de uma arvore nos pontos

## Files

- **genetic_algorithm.py**: Contém a implementação do Algoritmo Genético, incluindo funções para gerar populações, calcular a fitness, realizar operações de cruzamento e mutação e classificar populações com base na fitness.
- **tsp.py**: Implementa o TSP principal usando Pygame para visualização. Ele inicializa o problema, cria a população inicial e evolui iterativamente a população enquanto visualiza a melhor solução encontrada até o momento.
- **draw_functions.py**: Fornece funções para desenhar usando Pygame.

## Usage

Para rodar é necesário executar o `tsp.py` script usando Python.

## Dependencies

- Python 3.x
- Pygame (for visualization)
