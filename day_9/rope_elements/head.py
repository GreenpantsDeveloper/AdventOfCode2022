from typing import Tuple

from rope_elements.action import Action
from rope_elements.tail import Tail

"""
Let us view the grid as having the origin at the lower left:

(0, 2)   (1, 2)   (2, 2)
(0, 1)   (1, 1)   (2, 1)
(0, 0)   (1, 0)   (2, 0)
"""


class Head:
    def __init__(self):
        self.coordinates: Tuple[int, int] = (0, 0)
        self.tail = Tail()

    def move(self, direction: Action, rope_length: int = 1):
        """Move the head and the tail given a direction."""
        # Move the head.
        if direction == 'U':
            self.coordinates = (self.coordinates[0], self.coordinates[1] + 1)
        elif direction == 'D':
            self.coordinates = (self.coordinates[0], self.coordinates[1] - 1)
        elif direction == 'R':
            self.coordinates = (self.coordinates[0] + 1, self.coordinates[1])
        else:
            self.coordinates = (self.coordinates[0] - 1, self.coordinates[1])

        # Move the tail.
        self.tail.move(self.coordinates)
