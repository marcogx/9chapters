# Given number N which represents total number of leaves. Generate all possible trees,
# such that each node in tree has 0 or 2 children.
from binary_tree import TreeNode


def gen_zero_or_two_child_tree(n):
    if n <= 0:
        return []
    if n == 1:
        return [TreeNode(0)]

    res = []
    for i in xrange(1, n):
        ltrees = gen_zero_or_two_child_tree(i)
        rtrees = gen_zero_or_two_child_tree(n - i)
        for l in ltrees:
            for r in rtrees:
                root = TreeNode(0)
                root.left, root.right = l, r
                res.append(root)
    return res


def main():
    pass

if __name__ == '__main__':
    main()