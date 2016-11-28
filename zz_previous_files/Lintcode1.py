class Solution:
    """
    @param nums: A list of integers
    @param k: An integer denote to find k non-overlapping subarrays
    @return: An integer denote the sum of max k non-overlapping subarrays
    """
    # def maxSubArray(self, nums, k):
    #     if not nums or k <= 0 or k > len(nums):
    #         return float('-inf')
    #     n = len(nums)
    #     if k == n or k == 1:
    #        return sum(nums)
    #
    #     # sum of first i num
    #     sums = [0] * (n + 1)
    #     for i in xrange(1, n + 1):
    #         sums[i] = sums[i - 1] + nums[i - 1]
    #
    #     # max subarray sum for first i num when divided by j subarrays
    #     dp = [[float('-inf') for j in xrange(k + 1)] for i in xrange(n + 1)]
    #     for i in xrange(1, n + 1):
    #         for j in xrange(1, k + 1):
    #             if j > i:
    #                 dp[i][j] = float('-inf')
    #             elif j == i:
    #                 dp[i][j] = sums[i]
    #             else:
    #                 dp[i][j] = max([dp[x][j - 1] + self.max_once(nums[x:i]) for x in xrange(1, i)])
    #
    #     return dp[n][k]
    #
    # def max_once(self, nums):
    #     if True:
    #         if not nums:
    #             return float('-inf')
    #         n = len(nums)
    #         sums, minSum, maxDiff = [0] * (n + 1), 0, float('-inf')
    #         for i in xrange(1, n + 1):
    #             sums[i] = sums[i - 1] + nums[i - 1]
    #             maxDiff = max(maxDiff, sums[i] - minSum)
    #             minSum = min(minSum, sums[i])
    #         return maxDiff

    # def trailingZeroes(self, n):
    #     """
    #     :type n: int
    #     :rtype: int
    #     """
    #     if n == 0:
    #         return 1
    #     fac = 1
    #     for i in xrange(1, n + 1):
    #         fac *= i
    #     count = 0
    #     while fac % 10 == 0:
    #         count += 1
    #
    #     return count
    def rerange(self, A):
        if not A:
            return
        i, j, count = 0, len(A) - 1, 0
        for num in A:
            if num > 0:
                count += 1
        even, odd = 0, 1
        if len(A) % 2 == 1 and count == len(A) / 2:
            even, odd = 1, 0

        while i <= j:
            while i <=j and ((i % 2 == even and A[i] > 0) or
                    (i % 2 == odd and A[i] < 0)):
                i += 1
            while i <= j and ((j % 2 == even and A[j] > 0) or
                    (j % 2 == odd and A[j] < 0)):
                j -= 1
            if i > j:
                return
            else:
                A[i], A[j] = A[j], A[i]
                i += 1
                j -= 1

s = Solution()
A = [-13,-8,-12,-15,-14,35,7,-1,11,27,10,-7,-12,28,18]
print s.rerange(A)
print A
# print s.maxSubArray([-1,4,-2,3,-2,3], 2)