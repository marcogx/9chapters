# Given n, how many structurally unique BSTs (binary search trees) that store values 1...n?


def unique_bst(n):
    return unique_bst_recursion(1, n)


# TLE
def unique_bst_recursion(start, end):
    if start >= end:
        return 1
    res = 0
    for i in xrange(start, end + 1):
        l, r = unique_bst_recursion(start, i - 1), unique_bst_recursion(i + 1, end)
        res += l * r
    return res