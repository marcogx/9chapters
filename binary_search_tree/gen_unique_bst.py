from binary_tree import TreeNode


def gen_unique_bst(n):
    if n <= 0:
        return []
    return helper(1, n)


def helper(start, end):
    if start > end:
        return [None]
    if start == end:
        return [TreeNode(start)]

    res = []
    for i in xrange(start, end + 1):
        ltrees, rtrees = helper(start, i - 1), helper(i + 1, end)
        for l in ltrees:
            for r in rtrees:
                root = TreeNode(i)
                root.left, root.right = l, r
                res.append(root)
    return res


def main():
    pass

if __name__ == '__main__':
    main()