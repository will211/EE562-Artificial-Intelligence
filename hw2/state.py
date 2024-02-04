class State(object):
    """
    Constructor for the State class.

    Args:
        - vertex: The point with x and y value
        - g: Cost of the path from the initail state to this state
        - h: Cost from this state to the goal
        - f: Sum of the g and f
        - parent: The point parent
    """
    def __init__(self, vertex, g, h, parent):
        self.vertex = vertex
        self.g = g
        self.h = h
        self.f = self.g + self.h
        self.parent = parent

    def __repr__(self):
        return f"({self.vertex}, {self.g}, {self.h}, {self.f}, {self.parent})"

    def __eq__(self, other):
        return self.vertex == other.vertex