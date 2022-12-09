from typing import Tuple, List

from rope_elements.action import Action
from rope_elements.head import Head
from rope_elements.tail import Tail


def parse_actions(filename: str = "input.txt") -> List[Tuple[Action, int]]:
    """Turn input into tuples of actions."""
    with open(filename, 'r') as fp:
        return [(action, int(amount.strip())) for action, amount in
                [line.split(' ') for line in fp.readlines() if line]]


if __name__ == '__main__':
    # Define a rope with head and tail.
    rope = Head()

    # Parse the input file.
    actions = parse_actions()

    # Run each of the actions.
    for action, action_amount in actions:
        for _ in range(action_amount):
            rope.move(direction=action)

    # Solve challenge #1.
    print(f"Challenge #1: the tail has visited a total of {len(rope.tail.get_visited())} unique locations.")

    # ============================== #

    # Reset the rope.
    rope = Head()

    # Add multiple knots for challenge #2.
    last_tail = rope.tail
    for _ in range(8):
        last_tail.tail = Tail()
        last_tail = last_tail.tail  # Get the newly created tail's tail.

    # Run each of the actions.
    for action, action_amount in actions:
        for _ in range(action_amount):
            rope.move(direction=action)

    # Solve challenge #2.
    print(f"Challenge #2: the 10th knot has visited a total of {len(last_tail.get_visited())} unique locations.")
