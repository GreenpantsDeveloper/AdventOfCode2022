from abc import ABC
from typing import List


class Operation(ABC):
    """Abstract model of a CPU operation."""

    def __init__(self, name: str):
        self.name = name


class NoOp(Operation):
    """Model of the NOOP operation."""

    def __init__(self, name: str):
        super().__init__(name)


class AddX(Operation):
    """Model of the ADDX operation."""

    def __init__(self, name: str, value: int):
        super().__init__(name)
        self.value = value


Program = List[Operation]  # Type definition of a CPU program.
