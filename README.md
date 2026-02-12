# Algoritmos de Búsqueda y Optimización

Implementación de agentes inteligentes y algoritmos de optimización para la resolución de problemas de búsqueda en espacios de estados complejos.

Este repositorio contiene las soluciones desarrolladas para dos trabajos prácticos centrales, enfocados en búsqueda no informada/informada y metaheurísticas.

## Estructura del Proyecto

### 1. Búsqueda en Grafos (Pathfinding)
Implementación de algoritmos clásicos para encontrar caminos óptimos en un entorno de cuadrícula (Grid World) con obstáculos.
* **Ubicación:** Carpeta `tp-pathfinding`.
* **Algoritmos Implementados:**
    * Búsqueda en Anchura (BFS): Garantiza la solución más corta en grafos no ponderados.
    * Búsqueda en Profundidad (DFS): Exploración exhaustiva de ramas.
    * Búsqueda A* (A-Star): Uso de heurísticas (Distancia Manhattan/Euclídea) para optimizar el costo del camino.
    * Búsqueda Local (Hill Climbing): Optimización iterativa.

### 2. Problema del Viajante de Comercio (TSP) - Algoritmos Genéticos
Resolución del clásico problema de optimización combinatoria (Traveling Salesperson Problem) utilizando Computación Evolutiva.
* **Ubicación:** Carpeta `tp-tsp`.
* **Enfoque:** Se desarrolló un Algoritmo Genético para encontrar la ruta más corta que visita un conjunto de ciudades y regresa al origen.
* **Componentes del Algoritmo:**
    * Población Inicial: Generación aleatoria de rutas.
    * Función de Aptitud (Fitness): Inversa de la distancia total del recorrido.
    * Selección: Método de torneo o ruleta.
    * Cruzamiento (Crossover): Operadores para combinar rutas padres (ej: Order Crossover).
    * Mutación: Intercambio aleatorio de ciudades (Swap) para mantener diversidad genética.

## Documentación
Las consignas detalladas y restricciones de cada problema se encuentran en la carpeta `/docs`.

---
*Desarrollado en el marco de la asignatura Programación 3 / Inteligencia Artificial.*
