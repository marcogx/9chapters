def inorder(root):
    if not root:
        return []

    res, stack = [], []
    while root or stack:
        if root:
            stack.append(root)
            root = root.left
        else:
            root = stack.pop()
            res.append(root.val)
            root = root.right
    return res


def main():
    pass

if __name__ == '__main__':
    main()