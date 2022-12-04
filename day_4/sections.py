def parse_input(filename='input.txt'):
    """Build tuples with two ranges."""
    with open(filename, 'r') as fp:
        sections = [tuple(line.strip().split(',')) for line in fp.readlines()]

    return sections


def expand_range(range_string):
    """Turn a range string ('1-3') into a set of integers ({1, 2, 3})."""
    range_min, range_max = (int(x) for x in range_string.split('-'))
    return set(range(range_min, range_max + 1))  # Note the `range_max+1` to make the max inclusive :-)


if __name__ == '__main__':
    sections = parse_input()

    # Challenge #1.
    fully_contained_pairs = 0
    for section in sections:
        assignments_1, assignments_2 = (expand_range(section_range) for section_range in section)
        if not assignments_1 - assignments_2 or not assignments_2 - assignments_1:
            fully_contained_pairs += 1

    print(f"The number of assignment pairs where one range fully contains another is {fully_contained_pairs}.")

    # Challenge #2.
    any_overlapping_pairs = 0
    for section in sections:
        assignments_1, assignments_2 = (set(expand_range(section_range)) for section_range in section)
        if assignments_1.intersection(assignments_2) or assignments_2.intersection(assignments_1):
            any_overlapping_pairs += 1

    print(f"The number of assignment pairs where one range overlaps at all with another is {any_overlapping_pairs}.")
