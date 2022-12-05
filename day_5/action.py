import re


class Action:
    """Object representation of an action."""

    def __init__(self, action_line: str):
        """Create an Action given a string definition."""
        self.amount, self.from_stack, self.to_stack = (int(number) for number in re.findall(r'\d+', action_line))
