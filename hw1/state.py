class State(object):

    """
    Constructor for the State class.

    Args:
        - missionaries (int): Number of missionaries on the current state.
        - cannibals (int): Number of cannibals on the current state.
        - side (bool): The current state of the river side (True for left, False for right).
    """
    def __init__(self, missionaries, cannibals, side):
        self.missionaries = missionaries
        self.cannibals = cannibals
        self.side = side

    """
    Check if two State objects are equal.

    Args:
        - other (State): Another State object to compare.

    Returns:
        - bool: True if the two State objects are equal, False otherwise.
    """
    def __eq__(self, other):
        if self.missionaries == other.missionaries and self.cannibals == other.cannibals and self.side == other.side:
            return True
        else:
            return False

    """
    Generate a hash value for the State object.

    Returns:
        - int: A hash value based on the State's attributes.
    """
    def __hash__(self):
        return hash((self.missionaries, self.cannibals, self.side))

    """
    Convert the State object to a string representation.

    Returns:
        - str: A string representing the State in the format "missionaries, cannibals, side of the river".
    """
    def __str__(self):
        if self.side:
            return f"{self.missionaries}, {self.cannibals}, L"
        return f"{self.missionaries}, {self.cannibals}, R"