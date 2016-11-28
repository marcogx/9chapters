def is_symmetric(root):
    if not root:
        return True
    return mirror_compare(root.left, root.right)


def mirror_compare(left, right):
    if not left or not right:
        return left == right
    return (left.val == right.val and mirror_compare(left.left, right.right) and
            mirror_compare(left.right, right.left))