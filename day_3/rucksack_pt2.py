from rucksack import prio

GROUP_SIZE = 3


def parse_input(filename='input.txt'):
    """
    Parse the rucksacks input file for part day_2.

    :param filename: input filename.
    :return: rucksacks split by groups.
    """
    # Read the file.
    with open(filename, 'r') as fp:
        rucksacks = [line.strip() for line in fp.readlines()]

    # Group by three lines.
    return [rucksacks[i:i + GROUP_SIZE] for i in range(0, len(rucksacks), GROUP_SIZE)]


def find_badge(group):
    """
    Find an elf group's badge: the one overlapping item.

    :param group: Three rucksacks as a group of elves.
    :return: The matching badge item.
    """
    return (set(group[0]) & set(group[1]) & set(group[2])).pop()


if __name__ == '__main__':
    # Split rucksacks by groups.
    groups = parse_input()

    # Find the groups' badges.
    badges = [find_badge(group) for group in groups]

    # Compute the summed priorities for the badges.
    summed_prio = sum([prio(badge) for badge in badges])
    print(f"The sum of the priorities of the groups' badges is {summed_prio}.")
