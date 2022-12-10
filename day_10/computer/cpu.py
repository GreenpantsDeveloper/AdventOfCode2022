from computer.crt import CRT
from computer.operations import Program


class CPU:
    """Model for a simulated CPU."""
    def __init__(self):
        self.x = 1  # Value to perform operations on.
        self.num_cycles = 0
        self.signal_strength_sum = 0  # Challenge #1.
        self.crt = CRT()

    def cycle(self):
        """Perform a cycle update."""
        self.num_cycles += 1

        self.crt.draw(sprite_x=self.x)
        self.crt.print_screen()

        # Solve challenge #1.
        if (self.num_cycles - 20) % 40 == 0:
            self.signal_strength_sum += self.num_cycles * self.x

    def add_x(self, value: int):
        """Perform an ADDX operation."""
        self.x += value

    def run(self, program: Program):
        """Simulate running operations on the CPU."""
        for op in program:
            if op.name == "noop":
                # By definition: takes one cycle.
                self.cycle()

            elif op.name == "addx":
                # By definition: takes two cycles before addition is finalized.
                self.cycle()
                self.cycle()
                self.add_x(op.value)
