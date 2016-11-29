# Given two values k1 and k2 (where k1 < k2) and
# a root pointer to a Binary Search Tree.
# Find all the keys of tree in range k1 to k2.
# i.e. print all x such that k1<=x<=k2 and x is a key of given BST.
# Return all the keys in ascending order.


def search_range_inclusive(root, k1, k2):
    if not root or k1 > k2:
        return []
    res = []
    helper(root, k1, k2, res)
    return res


def helper(root, k1, k2, res):
    if not root:
        return
    val = root.val
    if val > k1:
        helper(root.left, k1, k2, res)
    if k1 <= val <= k2:
        res.append(val)
    if val < k2:
        helper(root.right, k1, k2, res)