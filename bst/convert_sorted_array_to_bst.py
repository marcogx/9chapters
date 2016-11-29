from binary_tree import TreeNode


def convert_sorted_array_to_bst(nums):
    if not nums:
        return None
    return build(nums, 0, len(nums) - 1)


def build(nums, start, end):
    if start > end:
        return None
    if start == end:
        return TreeNode(nums[start])

    mid = start + (end - start) / 2
    root = TreeNode(nums[mid])
    root.left = build(nums, start, mid - 1)
    root.right = build(nums, mid + 1, end)
    return root
