from vertex import Vertex
from state import State

class Solution(object):
    """
    Constructor for the Solution class.

    Args:
        - data: The input of the dataset
        - start_point: THe start state
        - goal_point: The goal state
        - obstacles: All the obstacles position
        - open: The open list for A * algorithm
        - close: The close list for A * algorithm
    """
    def __init__(self, data):
        self.data = data
        self.start_point = 0
        self.goal_point = 0
        self.obstacles = []
        self.open = {}
        self.close = {}
        self.parser()

    """
    Parse the data into the designated position

    """
    def parser(self):
        with open(self.data, 'r') as file:
            content = file.readlines()
            content = [line.rstrip().split(' ') for line in content]
            self.start_point = Vertex(content[0][0], content[0][1])
            self.goal_point = Vertex(content[1][0], content[1][1])

            for i in range(3, len(content)):
                line_obstacle = content[i]
                for j in range(0, 7 ,2):
                    self.obstacles.append([Vertex(line_obstacle[j], line_obstacle[j + 1])])
        
        self.a_star()

    """
    Compute the distance between two vertex

    Args:
        - x1: The first vertex x value
        - y1: The first vertex y value
        - x2: The Second vertex x value
        - y2: The Second vertex y value

    Returns:
        - The distance
    """
    def distance(self, x1, y1, x2, y2):
        return ((int(x1) - int(x2)) ** 2 + (int(y1) - int(y2)) ** 2) ** 0.5

    """
    Check if the line segment between two vertex that intersect the obstacles

    Args:
        - vertex_parent: The parent vertex
        - vertex_child: The child vertex

    Returns:
        - Ture if the state if valid, False otherwise
    """        
    def is_valid(self, vertex_parent, vertex_child):
        set_obstacles = []

        def line_intersect(vertex_parent, vertex_child, obstacle1, obstacle2):
            x1, y1 = int(vertex_parent.x), int(vertex_parent.y)
            x2, y2 = int(vertex_child.x), int(vertex_child.y)
            x3, y3 = obstacle1.to_list()
            x4, y4 = obstacle2.to_list()
            # Check if the rantangle obstacles intersect
            if min(x1, x2) >= max(x3, x4) or min(y1, y2) >= max(y3, y4) or \
                    min(x3, x4) >= max(x1, x2) or min(y3, y4) >= max(y1, y2):
                return False
            # Use the cross product to check for line segment intersection
            if ((y3 - y1) * (x2 - x1) - (x3 - x1) * (y2 - y1)) * ((y4 - y1) * (x2 - x1) - (x4 - x1) * (y2 - y1)) > 0:
                return False
            return True

        for i in range(0, len(self.obstacles), 4):
            set_obstacles.append([])
            set_obstacles[-1].append(self.obstacles[i])
            set_obstacles[-1].append(self.obstacles[i+1])
            set_obstacles[-1].append(self.obstacles[i+2])
            set_obstacles[-1].append(self.obstacles[i+3])

        for check in set_obstacles:

            if line_intersect(vertex_parent, vertex_child, check[0][0], check[2][0]) or \
                line_intersect(vertex_parent, vertex_child, check[1][0], check[3][0]):
                return False

        return True

    """
    Implement the A * algorithm and print the output

    """    
    def a_star(self):
        start_state = (State(self.start_point, 0, self.distance(self.start_point.x, self.start_point.y, self.goal_point.x, self.goal_point.y), self.start_point))
        self.open[self.start_point] = start_state

        while self.open:
            # Sort the open list with the f value
            self.open = dict(sorted(self.open.items(), key = lambda item: item[1].f))

            vertex_state, state = self.open.popitem()
            self.close[vertex_state] = state
            
            for child in self.obstacles:
                child = child[0]
                if self.is_valid(vertex_state, child):
                    g_of_child = state.g + self.distance(state.vertex.x, state.vertex.y, child.x, child.y)
                    h_of_child = self.distance(child.x, child.y, self.goal_point.x, self.goal_point.y)

                    # If the successor is already in the close list, If new f < previous f then remove from close list and add to open list 
                    if child in self.close:
                        if self.close[child].g > g_of_child:
                            del self.close[child]
                            self.open[child] = State(child, g_of_child, h_of_child, state.vertex)
                    
                    # If the successor is already in the open list, If new f < previous f then renew the open list
                    elif child in self.open:
                        if self.open[child].g > g_of_child:
                            self.open[child] = State(child, g_of_child, h_of_child, state.vertex)
                    else:
                        self.open[child] = State(child, g_of_child, h_of_child, vertex_state)

        itinerary = []
        itinerary_state = self.close[self.goal_point]
        while itinerary_state.vertex != self.start_point:
            itinerary.append(itinerary_state)
            itinerary_state = self.close[self.close[itinerary_state.vertex].parent]
        itinerary = itinerary[::-1]
        print("Point     Cumulative Cost")
        for state in ([itinerary_state] + itinerary):
            print(f"{str(state.vertex).ljust(10)} {state.g}")

def main():
    Solution("simple_dataset.txt")
    Solution("difficult_dataset.txt")
    Solution("customized_dataset.txt")

if __name__ == "__main__":
    main()