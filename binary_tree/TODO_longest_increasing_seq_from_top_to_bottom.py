def longest_increasing_seq_from_top_to_bottom(root):
    if not root:
        return 0
    longest = [1]
    helper(root, longest)
    return longest[0]


def helper(root, longest):
    if not root:
        return 0
    l, r = helper(root.left, longest), helper(root.right, longest)
    length = 1
    if root.left and root.left.val > root.val:
        length = 1 + l
    if root.right and root.right.val > root.val:
        length = max(length, 1 + r)

    longest[0] = max(longest[0], length)
    return length