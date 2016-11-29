# Given preorder and inorder traversal sequences of a tree, construct the binary tree.

from binary_tree import TreeNode


def construct_from_in_pre_order(preorder, inorder):
    if not preorder or not inorder:
        return None
    lpre, lin = len(preorder), len(inorder)
    if lpre != lin:
        return None
    return helper(preorder, 0, lpre, inorder, 0, lin)


def helper(preorder, pre_start, pre_end, inorder, in_start, in_end):
    if pre_start > pre_end:
        return None
    root_val = preorder[pre_start]
    root = TreeNode(root_val)
    if pre_start == pre_end:
        return root
    root_idx = inorder.index(root_val)
    left_size = (root_idx - 1) - in_start + 1
    left = helper(preorder, pre_start + 1, pre_start + left_size, inorder, in_start, root_idx - 1)
    right = helper(preorder, pre_start + left_size + 1, pre_end, inorder, root_idx + 1, in_end)
    root.left, root.right = left, right
    return root


def main():
    pass

if __name__ == '__main__':
    main()
