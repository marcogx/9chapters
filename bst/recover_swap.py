# Two elements of a binary search tree (BST) are swapped by mistake.
# Recover the tree without changing its structure.


def recover_swap(root):
    prev, pair = [None], [None, None]
    inorder(root, prev, pair)
    if pair[0]:
        pair[0].val, pair[1].val = pair[1].val, pair[0].val


def inorder(root, prev, pair):
    if not root:
        return
    inorder(root.left, prev, pair)
    if prev[0] and prev[0].val > root.val:
        if not pair[0]:
            pair[0] = prev[0]
        pair[1] = root
    prev[0] = root
    inorder(root.right, prev, pair)