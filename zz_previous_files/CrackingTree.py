

class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class STreeNode(object):
    def __init__(self, start, end, s):
        self.start, self.end, self.sum = start, end, s
        self.left, self.right = None, None


class Solution:
    """
    @param A, queries: Given an integer array and an Interval list
                       The ith query is [queries[i-1].start, queries[i-1].end]
    @return: The result list
    """
    def intervalSum(self, A, queries):
        if not A or not queries:
            return []
        root, ans = self.build(A, 0, len(A) - 1), []
        for q in queries:
            ans.append(self.query(root, q.start, q.end))
        return ans

    def build(self, A, start, end):
        if start == end:
            return STreeNode(start, end, A[start])
        mid = start + (end - start) / 2
        root = STreeNode(start, end, 0)
        root.left = self.build(A, start, mid)
        root.right = self.build(A, mid + 1, end)
        root.sum = root.left.sum + root.right.sum
        return root

    def query(self, root, start, end):
        # if start > end or start > root.end or end < root.start:
        #     return 0
        if start == root.start and end == root.end:
            return root.sum
        mid = root.start + (root.end - root.start) / 2
        if end <= mid:
            return self.query(root.left, start, end)
        elif start >= mid + 1:
            return self.query(root.right, start, end)
        else:
            return self.query(root.left, start, mid) + self.query(root.right, mid + 1, end)


interval = Interval(0, 0)
s = Solution()
A = [2,3,1,4,5]
print s.intervalSum(A, [interval])