def parse_input(filename='input.txt'):
    """
    Parse the rucksacks input file.

    :param filename: input filename.
    :return: rucksacks and their compartments.
    """
    with open(filename, 'r') as fp:
        rucksacks = [line.strip() for line in fp.readlines()]

    compartments = [(items[:len(items) // 2], items[len(items) // 2:]) for items in rucksacks]

    return compartments


def prio(char):
    """
    Get the priority of a character.

    :return: priority of a character.
    """
    if 'a' <= char <= 'z':
        return 1 + ord(char) - ord('a')
    if 'A' <= char <= 'Z':
        return 27 + ord(char) - ord('A')
    else:
        raise ValueError(f"Unsupported rucksack item: {char}")


if __name__ == '__main__':
    # Get rucksacks split by compartments
    rucksacks = parse_input()

    # Find the item that appears in both compartments.
    overlapping_items = [set(rucksack[0]) & set(rucksack[1]) for rucksack in rucksacks]

    # Compute the summed priorities.
    summed_prio = sum([prio(item_set.pop()) for item_set in overlapping_items])
    print(f"The sum of the priorities of overlapping compartment items is {summed_prio}.")
