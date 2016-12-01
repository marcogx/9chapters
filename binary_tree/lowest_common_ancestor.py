def lowest_common_ancestor(root, p, q):
    if not root:
        return None
    if root == p or root == q:
        return root
    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)
    if left and right:
        return root
    elif left:
        return left
    elif right:
        return right
    else:
        return None