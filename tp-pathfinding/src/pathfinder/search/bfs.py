from ..models.grid import Grid
from ..models.frontier import QueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class BreadthFirstSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Breadth First Search

        Args:
            grid (Grid): Grid of points
            
        Returns:
            Solution: Solution found
        """

        # Initialize a node with the initial position
        node = Node("", state=grid.start, cost=0, parent=None, action=None )

        # Initialize the explored dictionary to be empty
        explored = {} 
        # Add the node to the explored dictionary
        explored[node.state] = True
        
        # Initialize the frontier and add the node
        frontier = QueueFrontier()
        frontier.add(node)

        while True:

            # Fail if the frontier is empty
            if frontier.is_empty():
                return NoSolution(explored)

            n = frontier.remove()  # Remove a node from the frontier

            # Objective Test
            if n.state==grid.end:
                return Solution(n, explored)

            successors = grid.get_neighbours(n.state)  # Get its neighbours

            # For each possibly succesors, do:
            for act, res in successors.items():

                if res not in explored:
                    new_node = Node("", state=res, cost=n.cost + 1, parent=n, action=act)

                #if new_node.state == grid.end:
                 #   return Solution(new_node, explored)
            
                    explored[new_node.state] = True
                    frontier.add(new_node)
        

    
