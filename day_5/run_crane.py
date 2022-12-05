from typing import List, Tuple

from action import Action
from cargo import Cargo


def parse_input(filename='input.txt') -> Tuple[Cargo, List[Action]]:
    """Read the input file and turn this into Cargo and Action objects."""
    with open(filename, 'r') as fp:
        data = fp.read()

    # Split the cargo from the crane actions.
    cargo_data, actions_data = data.split('\n\n')

    cargo = Cargo(cargo_data.split('\n'))
    actions = [Action(action_line) for action_line in actions_data.split('\n') if action_line]

    return cargo, actions


if __name__ == '__main__':
    # ===== Part 1: using CrateMover 9000 ===== #
    cargo, actions = parse_input()

    for action in actions:
        cargo.move(action)

    cargo_tops = cargo.get_top()
    print(f"The top of each stack for CraneMover 9000 is:\n> '{cargo_tops}'\n")

    # ===== Part 2: using CrateMover 9001 ===== #
    cargo, actions = parse_input()

    for action in actions:
        cargo.move_multiple(action)

    cargo_tops = cargo.get_top()
    print(f"The top of each stack for CraneMover 9001 is:\n> '{cargo_tops}'")
