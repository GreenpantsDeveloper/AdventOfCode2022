import numpy as np


class CRT:
    """Model for a CRT display."""

    def __init__(self):
        self.screen = np.full((6, 40), ' ')
        self.x = 0
        self.y = 0

    def draw(self, sprite_x):
        """Draw the next position."""
        self.screen[self.y][self.x] = '.' if abs(sprite_x - self.x) > 1 else '#'

        # Update drawing position.
        if self.x >= self.screen.shape[1] - 1:
            self.x = 0
            self.y += 1
        else:
            self.x += 1

    def next_line(self):
        """Skip to the next line."""
        self.y += 1

    def print_screen(self):
        """Draw the CRT output in the terminal."""
        print()  # An additional newline is always 'preciated :-)
        for line in self.screen:
            print("".join(line))
