def count_cbt_nodes(root):
    if not root:
        return 0
    lh, rh = get_left(root.left), get_left(root.right)
    if lh == rh:
        return 1 + (1 << lh) - 1 + count_cbt_nodes(root.right)
    else:
        return 1 + (1 << rh) - 1 + count_cbt_nodes(root.left)


def get_left(root):
    res = 0
    while root:
        res += 1
        root = root.left
    return res
