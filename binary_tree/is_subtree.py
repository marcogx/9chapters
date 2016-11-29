# Given two binary trees, check if the first tree is subtree of the second one.
# A subtree of a tree L is a tree S consisting of a node in L
# and all of its descendants in L.
# The subtree corresponding to the root node is the entire tree;
# the subtree corresponding to any other node is called a proper subtree

# O(L + S) solution using inorder and preorder and sub array matching to check "is part of"
# by marking None child to solve "is subtree of".
# http://www.geeksforgeeks.org/check-binary-tree-subtree-another-binary-tree-set-2/
from binary_tree.is_same import is_same


def is_subtree(L, S):
    if not S:
        return True
    if not L:
        return False
    if is_same(L, S):
        return True
    return is_subtree(L.left, S) or is_subtree(L.right, S)
