from binary_tree import TreeNode


def construct_from_in_post_order(postorder, inorder):
    if not inorder or not postorder:
        return None
    lpost, lin = len(postorder), len(inorder)
    if lpost != lin:
        return None
    return helper(postorder, 0, lpost - 1, inorder, 0, lin - 1)


def helper(postorder, post_start, post_end, inorder, in_start, in_end):
    if post_start > post_end:
        return None

    root_val = postorder[post_end]
    root = TreeNode(root_val)
    if post_start == post_end:
        return root
    root_idx = inorder.index(root_val)
    left_size = root_idx - 1 - in_start + 1
    left = helper(postorder, post_start, post_start + left_size - 1, inorder, in_start, root_idx - 1)
    right = helper(postorder, post_start + left_size, post_end - 1, inorder, root_idx + 1, in_end)
    root.left, root.right = left, right
    return root


def main():
    pass

if __name__ == '__main__':
    main()