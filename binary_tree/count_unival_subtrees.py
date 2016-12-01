def count_unival_subtrees(root):
    if not root:
        return 0

    count = [0]
    helper(root, float('inf'), count)
    return count[0]


def helper(root, target, count):
    if not root:
        return True

    l, r = helper(root.left, root.val, count), helper(root.right, root.val, count)
    if not l or not r:
        return False

    count[0] += 1
    return root.val == target
