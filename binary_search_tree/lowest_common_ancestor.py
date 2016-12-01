def lowest_common_ancestor(root, p, q):
    if not root:
        return None
    if root == p or root == q:
        return root
    s, l = min(p.val, q.val), max(p.val, q.val)
    if s < root.val < l:
        return root
    if l < root.val:
        return lowest_common_ancestor(root.left, p, q)
    if root.val < s:
        return lowest_common_ancestor(root.right, p, q)
