import numpy as np


def load_trees(filename="input.txt"):
    """Load the file as a 2D numpy array."""
    with open(filename, 'r') as fp:
        trees = np.array([[int(digit) for digit in line.strip()] for line in fp.readlines()])

    return trees


def is_visible(trees: np.ndarray, row: int, col: int) -> int:
    """Return 0 or 1 whether a tree is visible from outside the grid."""
    if row == 0 or col == 0 or row == trees.shape[1] - 1 or col == trees.shape[0] - 1:
        # Tree is at the edge.
        return 1

    tree_height = trees[row][col]

    # Check left.
    if np.max(trees[row, :col]) < tree_height:
        return 1

    # Check right.
    elif np.max(trees[row, col + 1:]) < tree_height:
        return 1

    # Check above.
    elif np.max(trees[:row, col]) < tree_height:
        return 1

    # Check below.
    elif np.max(trees[row + 1:, col]) < tree_height:
        return 1

    return 0


def compute_scenic_score(trees: np.ndarray, row: int, col: int) -> int:
    """Compute the scenic score of a tree."""
    if row == 0 or col == 0 or row == trees.shape[1] - 1 or col == trees.shape[0] - 1:
        # Tree is at the edge; score will be multiplied by 0.
        return 0

    tree_height = trees[row][col]

    # Get separate arrays in the right order for each direction.
    trees_left = trees[row, :col][::-1]  # reversed
    trees_right = trees[row, col + 1:]
    trees_above = trees[:row, col][::-1]  # reversed
    trees_below = trees[row + 1:, col]

    # Multiply the scenic scores for each direction.
    scenic_score = 1
    for trees in (trees_left, trees_right, trees_above, trees_below):
        scenic_score *= find_nearest_tall_tree(trees, tree_height)

    return scenic_score


def find_nearest_tall_tree(trees: np.ndarray, tree_height: int) -> int:
    """Find the index of the nearest tree in the array that is at least as tall as the input tree."""
    for i, near_tree in enumerate(trees):
        if near_tree >= tree_height:
            return i + 1

    # No tree at least as tall? We have a clear view!
    return len(trees)


if __name__ == '__main__':
    trees = load_trees()

    num_visible = 0
    scenic_scores = np.zeros(trees.shape)

    for row in range(trees.shape[0]):
        for col in range(trees.shape[1]):
            num_visible += is_visible(trees, row, col)
            scenic_scores[row][col] = compute_scenic_score(trees, row, col)

    print(f"The number of visible trees is {num_visible}.")
    print(f"The highest scenic score available is {int(np.max(scenic_scores))}.")
