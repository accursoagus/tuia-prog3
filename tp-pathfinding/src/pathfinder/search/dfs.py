from ..models.grid import Grid
from ..models.frontier import StackFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class DepthFirstSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Depth First Search

        Args:
            grid (Grid): Grid of points
            
        Returns:
            Solution: Solution found
        """
        # Initialize a node with the initial position
        node = Node("", grid.start, 0)

        # Si el nodo inicial ya es la meta, retornar solución
        if node.state == grid.end:
            return Solution(node, explored={node.state: True})

        # Initialize the explored dictionary to be empty
        explored = {} 
        
        # Inicializar frontera como una pila (LIFO)
        frontier = StackFrontier()
        frontier.add(node)


        # Add the node to the explored dictionary
        explored[node.state] = True

        while not frontier.is_empty():
            # Extraer el nodo más reciente de la pila
            node = frontier.remove()

            # Expandir nodo
            for action, new_state in grid.get_neighbours(node.state).items():
                if new_state in explored:
                    continue

                new_node = Node("", state=new_state, cost=node.cost + grid.get_cost(new_state), parent=node, action=action)

                # Si es la meta, retornar la solución
                if new_node.state == grid.end:
                    return Solution(new_node, explored)

                # Marcar como explorado y agregarlo a la frontera
                explored[new_node.state] = True
                frontier.add(new_node)

        return NoSolution(explored)

