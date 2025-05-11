from ..models.grid import Grid
from ..models.frontier import PriorityQueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node

class GreedyBestFirstSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Greedy Best First Search

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """
        # Initialize a node with the initial position
        node = Node("", grid.start, 0)

        # Initialize the explored dictionary to be empty
        explored = {} 
        
        # Add the node to the explored dictionary
        explored[node.state] = node.cost

        frontier = PriorityQueueFrontier()
        frontier.add(node, grid.my_heuristic(node, grid.end))

        while not frontier.is_empty():
            n = frontier.pop()

            # test objetivo
            if n.state == grid.end:
                return Solution(n, explored)

            successors = grid.get_neighbours(n.state)
        
            for act, res in successors.items():
                #sí aún no lo exploré o ya lo exploré con un costo de camino mayor, lo tengo en cuenta
                if res not in explored or n.cost + grid.get_cost(res) < explored[res]:
                    new_node = Node("", state=res, cost=n.cost + grid.get_cost(res), parent=n, action=act)

                    explored[new_node.state] = new_node.cost
                    frontier.add(new_node, grid.my_heuristic(new_node, grid.end))


        return NoSolution(explored)
