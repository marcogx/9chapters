from depth import max_depth
from binary_search_tree.gen_unique_bst import gen_unique_bst


def is_balanced(root):
    if not root:
        return True
    l, r = max_depth(root.left), max_depth(root.right)
    return abs(l - r) <= 1 and is_balanced(root.left) and is_balanced(root.right)


def main():
    trees = gen_unique_bst(3)
    for root in trees:
        print is_balanced(root)


if __name__ == '__main__':
    main()