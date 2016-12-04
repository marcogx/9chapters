def populate_next_right_pointer_perfect_tree(root):
    if not root or (not root.left and not root.right):
        return
    if root.left:
        root.left.next = root.right
        if root.next:
            root.right.next = root.next.left
        populate_next_right_pointer_perfect_tree(root.left)
        populate_next_right_pointer_perfect_tree(root.right)
