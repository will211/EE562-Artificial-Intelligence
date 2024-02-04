class Vertex(object):
    """
    Constructor for the Vertex class.

    Args:
        - x: The point of Vertex x value
        - y: The point of Vertex y value
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f"({self.x}, {self.y})"

    def __eq__(self, other):
        return other.x == self.x and other.y == self.y
    
    def __hash__(self):
        return hash((self.x, self.y))

    def to_list(self):
        return [int(self.x), int(self.y)]