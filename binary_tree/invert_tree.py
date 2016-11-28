def invert_tree(root):
    if not root:
        return None
    l, r = invert_tree(root.left), invert_tree(root.right)
    root.left, root.right = r, l
    return root