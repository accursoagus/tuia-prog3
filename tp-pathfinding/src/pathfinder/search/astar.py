from ..models.grid import Grid
from ..models.frontier import PriorityQueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node

def my_heuristic(node: Node, goal) -> int:
    # favorecemos los movimientos que van hacia abajo a la derecha
  x,y = node.state
  i,j = goal
  return abs(x-i)+abs(j-y)

class AStarSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using A* Search

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
        frontier.add(node, node.cost+my_heuristic(node, grid.end))

        while not frontier.is_empty():
            n = frontier.pop()

            if n.state == grid.end:
                return Solution(n, explored)

            successors = grid.get_neighbours(n.state)
        
            for act, res in successors.items():

                if res not in explored or n.cost + grid.get_cost(res) < explored[res]:
                    new_node = Node("", state=res, cost=n.cost + grid.get_cost(res), parent=n, action=act)

                    explored[new_node.state] = new_node.cost
                    frontier.add(new_node, new_node.cost+my_heuristic(new_node, grid.end))


        return NoSolution(explored)
