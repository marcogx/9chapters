from bst.gen_unique_bst import gen_unique_bst


# The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
def max_depth(root):
    if not root:
        return 0
    return max(max_depth(root.left), max_depth(root.right)) + 1


# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
def min_depth(root):
    if not root:
        return 0
    left, right = min_depth(root.left), min_depth(root.right)
    return left + right + 1 if left == 0 or right == 0 else min(left, right) + 1


def main():
    trees = gen_unique_bst(3)
    for root in trees:
        print max_depth(root), min_depth(root)


if __name__ == '__main__':
    main()
