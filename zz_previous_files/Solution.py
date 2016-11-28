class Solution(object):
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        fas, sizes, ans, lands = [i for i in xrange(m * n)], [0 for i in xrange(m * n)], [], []
        for p in positions:
            idx = p[0] * n + p[1]
            sizes[idx] = 1
            lands.append(idx)
            for j in self.adj_lands(m, n, idx, sizes):
                self.union(fas, idx, j, sizes)
            vals = [self.find(i, fas) for i in lands]
            sets = set(vals)
            ans.append(len(sets))

        return ans

    def adj_lands(self, m, n, idx, sizes):
        r, c, ans = idx / n, idx % n, []
        u, d, l, right = (r - 1) * n + c, (r + 1) * n + c, r * n + c - 1, r * n + c + 1
        if r - 1 >= 0 and sizes[u]:
            ans.append(u)
        if r + 1 < m and sizes[d]:
            ans.append(d)
        if c - 1 >= 0 and sizes[l]:
            ans.append(l)
        if c + 1 < n and sizes[right]:
            ans.append(right)
        return ans

    def find(self, idx, fas):
        fa, cur = fas[idx], idx
        if cur != fa:
            cur = fas[fa]
            fa = fas[cur]
        # fas[idx] = fa
        return fa

    def compress_find(self, idx, fas):
        root = self.find(idx, fas)
        fa = fas[idx]
        while fa != root:
            fas[idx] = root
            idx = fa
            fa = fas[idx]
        return root


    def union(self, fas, i, j, sizes):
        rooti, rootj = self.compress_find(i, fas), self.compress_find(j, fas)
        if rooti != rootj:
            if sizes[i] >= sizes[j]:
                fas[rootj] = rooti
                sizes[rooti] += sizes[rootj]
            else:
                fas[rooti] = rootj
                sizes[rootj] += sizes[rooti]

s = Solution()
print s.numIslands2(5, 10, [[4,9],[4,8]])