from ..models.grid import Grid
from ..models.frontier import PriorityQueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class UniformCostSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Uniform Cost Search

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """
        # Initialize a node with the initial position
        node = Node("", state=grid.start, cost=0 , parent=None, action=None )

        # Initialize the frontier and add the node
        frontier = PriorityQueueFrontier()
        frontier.add(node, node.cost)

        # Initialize the explored dictionary to be empty
        explored = {} 
        # Add the node to the explored dictionary
        explored[node.state] = node.cost

        while not frontier.is_empty():

            n = frontier.pop() # Remove a node from the frontier

            # Objective Test
            if n.state==grid.end:
                return Solution(n, explored)

            successors = grid.get_neighbours(n.state) # Get its neighbours

            # For each possibly succesors, do:
            for act, res in successors.items():
                #sí aún no lo exploré o ya lo exploré con un costo de camino mayor, lo tengo en cuenta
                if res not in explored or n.cost + grid.get_cost(res) < explored[res]:
                    new_node = Node("", state=res, cost=n.cost + grid.get_cost(res), parent=n, action=act)

                    explored[new_node.state] = new_node.cost
                    frontier.add(new_node, new_node.cost)

        return NoSolution(explored)
