def preorder(root):
    if not root:
        return []

    res, stack = [], []
    while root or stack:
        if root:
            res.append(root.val)
            stack.append(root)
            root = root.left
        else:
            root = stack.pop()
            root = root.right

    return res


def main():
    pass

if __name__ == '__main__':
    main()