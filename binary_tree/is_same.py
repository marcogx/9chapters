def is_same(left, right):
    if not left or not right:
        return left == right
    return (left.val == right.val and is_same(left.left, right.right) and
            is_same(left.right, right.right))