# Given a binary tree, find the length of the longest consecutive sequence path.
# The path refers to any sequence of nodes from some starting node to any node
# in the tree along the parent-child connections.
# The longest consecutive path need to be from parent to child (cannot be the reverse).


def longest_consecutive_seq(root):
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
    if root.left and root.left.val == root.val + 1:
        length = 1 + l
    if root.right and root.right.val == root.val + 1:
        length = max(length, 1 + r)

    longest[0] = max(longest[0], length)
    return length