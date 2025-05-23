"""Este modulo define la clase LocalSearch.

LocalSearch representa un algoritmo de busqueda local general.

Las subclases que se encuentran en este modulo son:

* HillClimbing: algoritmo de ascension de colinas. Se mueve al sucesor con
mejor valor objetivo. Ya viene implementado.

* HillClimbingReset: algoritmo de ascension de colinas de reinicio aleatorio.
No viene implementado, se debe completar.

* Tabu: algoritmo de busqueda tabu.
No viene implementado, se debe completar.
"""


from __future__ import annotations
from time import time
from problem import OptProblem


class LocalSearch:
    """Clase que representa un algoritmo de busqueda local general."""

    def __init__(self) -> None:
        """Construye una instancia de la clase."""
        self.niters = 0  # Numero de iteraciones totales
        self.time = 0  # Tiempo de ejecucion
        self.tour = []  # Solucion, inicialmente vacia
        self.value = None  # Valor objetivo de la solucion

    def solve(self, problem: OptProblem):
        """Resuelve un problema de optimizacion."""
        self.tour = problem.init
        self.value = problem.obj_val(problem.init)


class HillClimbing(LocalSearch):
    """Clase que representa un algoritmo de ascension de colinas.

    En cada iteracion se mueve al estado sucesor con mejor valor objetivo.
    El criterio de parada es alcanzar un optimo local.
    """

    def solve(self, problem: OptProblem):
        """Resuelve un problema de optimizacion con ascension de colinas.

        Argumentos:
        ==========
        problem: OptProblem
            un problema de optimizacion
        """
        # Inicio del reloj
        start = time()

        # Arrancamos del estado inicial
        actual = problem.init
        value = problem.obj_val(problem.init)

        while True:

            # Buscamos la acción que genera el sucesor con mayor valor objetivo
            act, succ_val = problem.max_action(actual)

            # Retornar si estamos en un maximo local:
            # el valor objetivo del sucesor es menor o igual al del estado actual
            if succ_val <= value:

                self.tour = actual
                self.value = value
                end = time()
                self.time = end-start
                return

            # Sino, nos movemos al sucesor
            actual = problem.result(actual, act)
            value = succ_val
            self.niters += 1


class HillClimbingReset(LocalSearch):
    """Algoritmo de ascension de colinas con reinicio aleatorio."""
    def __init__(self):
         super().__init__()
         self.max_reset = 10
    
    def solve(self, problem: OptProblem):
        start = time()
        self.niters = 0

        actual = problem.init
        value = problem.obj_val(problem.init)
        self.niters += 1
        best_tour = actual
        best_value = value

        for _ in range(self.max_reset):
            while True:
                    act, succ_val = problem.max_action(actual)
                    if succ_val <= value:
                        break
                    actual = problem.result(actual, act)
                    value = succ_val
                    self.niters += 1

            if value > best_value:
                best_value = value
                best_tour = actual

            actual = problem.random_reset()
            value = problem.obj_val(actual)

        self.tour = best_tour
        self.value = best_value
        end = time()
        self.time = end - start


class Tabu(LocalSearch):
    """Algoritmo de busqueda tabu."""
    def __init__(self):
        super().__init__()
        self.max_iters = 100
        self.tenure = 15
        self.tabu_list = []

    def solve(self, problem: OptProblem):
        start = time()
        actual = problem.init
        value = problem.obj_val(actual)
        best_tour = actual
        best_value = value

        self.niters = 0

        while self.niters < self.max_iters:
            act, succ_val = problem.max_action(actual, self.tabu_list, best_value)
            succ = problem.result(actual, act)

            #actualizo lista tabú, si está llena saco el elemento más antiguo
            self.tabu_list.append(act)
            if len(self.tabu_list) > self.tenure:
                self.tabu_list.pop(0)
                
            #actualizo estado actual    
            actual = succ
            value = succ_val
            self.niters += 1

            # gaurdo el mejor
            if value > best_value:
                best_value = value
                best_tour = actual

        self.tour = best_tour
        self.value = best_value
        end = time()
        self.time = end - start