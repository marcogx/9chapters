from depth import max_depth


def is_balanced(root):
    if not root:
        return True
    l, r = max_depth(root.left), max_depth(root.right)
    return abs(l - r) <= 1 and is_balanced(root.left) and is_balanced(root.right)
