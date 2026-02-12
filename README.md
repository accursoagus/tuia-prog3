# Algoritmos de Búsqueda y Optimización

Implementación de agentes inteligentes y algoritmos de optimización para la resolución de problemas de búsqueda en espacios de estados complejos. Este repositorio contiene las soluciones desarrolladas para dos trabajos prácticos centrales, enfocados en búsqueda no informada/informada y metaheurísticas.

## Estructura del Proyecto

### 1. Búsqueda en Grafos (Pathfinding)
Implementación de algoritmos clásicos para encontrar caminos óptimos en un entorno de cuadrícula (**Grid World**) con obstáculos.

- **Ubicación:** Carpeta `tp-pathfinding`.
- **Algoritmos Implementados:**
  - **Búsqueda en Anchura (BFS):** Garantiza la solución más corta en grafos no ponderados.
  - **Búsqueda en Profundidad (DFS):** Exploración exhaustiva de ramas.
  - **Búsqueda A* (A-Star):** Uso de heurísticas (Distancia Manhattan/Euclídea) para optimizar el costo del camino.
  - **Búsqueda Local (Hill Climbing):** Optimización iterativa.

### 2. Problema del Viajante de Comercio (TSP) - Algoritmos Genéticos
Resolución del clásico problema de optimización combinatoria (**Traveling Salesperson Problem**) aplicado a la logística en Argentina.

- **Ubicación:** Carpeta `tp-tsp`.
- **Desafío:** Encontrar la ruta óptima que visite las 23 capitales de provincia + CABA y regrese al origen, minimizando la distancia total.
- **Enfoque:** Se desarrolló un Algoritmo Genético "from scratch" con los siguientes componentes:
  1. **Población Inicial:** Generación aleatoria de permutaciones (rutas).
  2. **Función de Aptitud (Fitness):** Inversa de la distancia total del recorrido.
  3. **Selección:** Implementación de métodos de torneo o ruleta.
  4. **Cruzamiento (Crossover):** Operadores para combinar rutas (ej: Order Crossover) preservando la validez del camino.
  5. **Mutación:** Intercambio aleatorio de ciudades (Swap) para mantener diversidad genética.

## Tecnologías Utilizadas

- **Python 3**
- **Matplotlib** (Visualización de rutas y convergencia)
- **NumPy / Pandas**
- Implementación propia de algoritmos evolutivos (sin frameworks externos)

## Documentación

Las consignas detalladas y restricciones de cada problema se encuentran en la carpeta `/docs`.

> Desarrollado en el marco de la asignatura **Programación 3 / Inteligencia Artificial**.
