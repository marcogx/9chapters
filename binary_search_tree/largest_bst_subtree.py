def largest_bst_subtree(root):
    if not root:
        return 0
    res = [1]
    helper(root, res)
    return res[0]


def helper(root, res):
    if not root:
        return 0, 0, 0
    l, r = helper(root.left, res), helper(root.right, res)
    if not l or not r:
        return None
    val = root.val
    if l[2] > 0 and l[1] > val or r[2] > 0 and val > r[0]:
        return None

    min_val = l[0] if l[2] > 0 else val
    max_val = r[1] if r[2] > 0 else val
    size = l[2] + r[2] + 1
    res[0] = max(res[0], size)
    return min_val, max_val, size
