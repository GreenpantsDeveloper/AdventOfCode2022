from typing import Tuple, Set, Optional


class Tail:
    def __init__(self, tail: Optional["Tail"] = None):
        self.coordinates: Tuple[int, int] = (0, 0)
        self.visited: Set[Tuple[int, int]] = set()
        self.visited.add(self.coordinates)  # Keep the set from interpreting the tuple as an iterable.
        self.tail = tail

    def move(self, head_coordinates: Tuple[int, int]):
        """Move the tail following the new coordinates."""
        x_diff = head_coordinates[0] - self.coordinates[0]
        y_diff = head_coordinates[1] - self.coordinates[1]

        # Check if we have to move along the x-axis.
        if abs(x_diff) > 1:
            # Check if we have to move diagonally.
            if abs(y_diff) >= 1:
                self.coordinates = (self.coordinates[0]), self.coordinates[1] + int(y_diff / abs(y_diff))
            self.coordinates = (self.coordinates[0] + int(x_diff / abs(x_diff)), self.coordinates[1])

        # Check if we have to move along the y-axis.
        elif abs(y_diff) > 1:  # Side note: I spent half an hour debugging because I made this an 'if' instead of 'elif'
            # Check if we have to move diagonally.
            if abs(x_diff) >= 1:
                self.coordinates = (self.coordinates[0] + int(x_diff / abs(x_diff)), self.coordinates[1])
            self.coordinates = (self.coordinates[0], self.coordinates[1] + int(y_diff / abs(y_diff)))

        # Update the set of visited coordinates.
        self.visited.add(self.coordinates)

        # Move an optional sub-tail.
        if self.tail:
            self.tail.move(self.coordinates)

    def get_visited(self):
        """Neat ole' getter for the set of visited coordinates."""
        return self.visited
