from typing import List, Any

from action import Action

CARGO_LINE_LENGTH = 35  # helper for parsing the cargo lines


class Cargo:
    """Object definition of stacks of cargo."""

    def __init__(self, cargo_lines: List[str]):
        self.crane_model = "CrateMover 9001"
        self.stacks = self.__parse_cargo(cargo_lines)

    def move(self, action: Action):
        """Perform an action on the cargo stacks."""
        for _ in range(action.amount):
            # Note how cargo starts at number 1 whereas our stacks start at index 0.
            crate = self.stacks[action.from_stack - 1].pop()
            self.stacks[action.to_stack - 1].append(crate)

    def move_multiple(self, action: Action):
        """NOTE: ONLY AVAILABLE FOR CrateMover 9001."""
        assert self.crane_model != "CrateMover 9000", "move_multiple() is not supported on this crane!"  # :-)

        crates = reversed([self.stacks[action.from_stack - 1].pop() for _ in range(action.amount)])
        for crate in crates:
            self.stacks[action.to_stack - 1].append(crate)

    def get_top(self) -> str:
        """Give a string representation of the tops of the stacks."""
        tops = [stack[-1] for stack in self.stacks]
        return "".join(tops)

    @staticmethod
    def __parse_cargo(cargo_lines) -> List[List[str]]:
        """Turn the cargo definition into stacks of crates."""
        stack_lines = cargo_lines[:-1]
        line_of_crates = [[line[i] for i in range(1, CARGO_LINE_LENGTH, 4)] for line in stack_lines]

        # Change horizontal crate definition to vertical, i.e. stacks.
        stacks = _transpose(line_of_crates)

        # Stack popping requires reverse order.
        stacks = [reversed(stack) for stack in stacks]

        # Remove air (non-crates) from the stacks.
        stacks = [list(filter(lambda c: c != ' ', stack)) for stack in stacks]

        return stacks


def _transpose(list_: List[List[Any]]) -> List[List[Any]]:
    """Transpose a given list."""
    return [[row[i] for row in list_] for i in range(len(list_[0]))]
