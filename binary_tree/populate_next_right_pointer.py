from binary_tree import TreeLinkNode


def populate_next_right_pointer(root):
    dummy = TreeLinkNode(-1)
    pre = dummy
    while root:
        if root.left:
            pre.next = root.left
            pre = pre.next
        if root.right:
            pre.next = root.right
            pre = pre.next
        root = root.next
        if not root:
            if pre == dummy:
                break
            root, pre = dummy.next, dummy