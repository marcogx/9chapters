def postorder(root):
    if not root:
        return []

    res, stack = [], []
    while root or stack:
        if root:
            res.append(root.val)
            stack.append(root)
            root = root.right
        else:
            root = stack.pop()
            root = root.left

    res.reverse()
    return res


def main():
    pass

if __name__ == '__main__':
    main()