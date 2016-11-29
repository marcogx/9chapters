def is_valid_bst(root):
    # return preorder(root, float('-inf'), float('inf'))[0]
    # return postorder(root)
    return inorder(root, [None])


def inorder(root, prev):
    if not root:
        return True

    if not inorder(root.left, prev):
        return False
    if prev[0] and prev[0].val >= root.val:
        return False
    prev[0] = root
    return inorder(root.right, prev)


def preorder(root, lbound, rbound):
    if not root:
        return True
    return (lbound < root.val < rbound and preorder(root.left, lbound, root.val) and
            preorder(root.right, root.val, rbound))


def postorder(root):
    if not root:
        return True, float('inf'), float('-inf')
    left, right = postorder(root.left), postorder(root.right)
    is_bst = left[0] and right[0] and left[2] < root.val < right[1]
    return is_bst, min(root.val, left[1]), max(root.val, right[2])


def main():
    pass


if __name__ == '__main__':
    main()
