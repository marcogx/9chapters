# You can perform AT MOST one move on the array: choose any two integers [L, R],
# and flip all the elements between (and including) the L-th and R-th bits. L and
# R represent the left-most and right-most index of the bits marking the
# boundaries of the segment which you have decided to flip.
#

# the final bit-string?
# a bit means, that a 0 is transformed to a 1 and a 1 is transformed to
# a 0
# Input Format
# An integer N
# Next line contains the N bits, separated by spaces: d[0] d[1] d[N-1]
#
# Output:
# S
#
# Sample Input:
# 8
# 1 0 0 1 0 0 1 0
# Sample Output:
# 6


# def flip_max(bits):
# 	if not bits:
# 		return 0
#
# 	ones, diff, max_diff = 0, 0, 0
# 	for bit in bits:
# 		if bit == 0:
# 			diff += 1
# 		else:
# 			ones += 1
# 			diff -= 1
# 		diff = max(diff, 0)
# 		max_diff = max(max_diff, diff)
#
# 	return ones + max_diff
#
#
# N = input()
# bits = [int(_) for _ in raw_input().split()]
# print flip_max(bits)

# Input Format:
# N -number of leaves
# A - Given array of integers
#
# Output Format:
# An integer denoting the number of uneaten leaves.
#
# Sample Input:
# N = 10
# A = [2,4,5]
#
# Sample Output:
# 4


# def uneaten_leaves(N, A):
# 	subsets, total = get_subsets(A, N), 0
# 	for ss in subsets:
# 		eaten = N // ss[1]
# 		# inclusion-exclusion principle
# 		total += eaten if ss[0] % 2 == 1 else -eaten
# 	return N - total
#
#
# def get_subsets(A, N):
# 	ans = []
# 	subsets_helper(ans, [], A, 0, 1, N)
# 	ans.pop(0)  # del the empty set
# 	return ans
#
#
# def subsets_helper(ans, cur, A, start, lcm, N):
# 	# only record the len and lcm of each subset
# 	if lcm > N:
# 		return
# 	ans.append((len(cur), lcm))
# 	for i in xrange(start, len(A)):
# 		cur.append(A[i])
# 		# recursively compute lcm of subset, lcm(a, b, c) = lcm(lcm(a, b), c)
# 		subsets_helper(ans, cur, A, i + 1, get_lcm(lcm, A[i]), N)
# 		cur.pop()
#
#
# def gcd(a, b):
# 	while b:
# 		a, b = b, a % b
# 	return a
#
#
# def get_lcm(a, b):
# 	if a == 0 and b == 0:
# 		return 0
# 	return a * b / gcd(a, b)
#
#
# N = input()
# A = [int(_) for _ in raw_input().split()]
# print uneaten_leaves(N, A)
#
class Solution:

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m, n = len(nums1), len(nums2)
        sz = m + n
        nums, i, j, idx = [0] * (sz), 0, 0, 0

        while i < m and j < n:
            if nums1[i] < nums2[j]:
                nums[idx] = nums1[i]
                i += 1
            else:
                nums[idx] = nums2[j]
                j += 1
            idx += 1

        if i < m:
            nums[idx] = nums1[i]
            i += 1; idx += 1
        if j < n:
            nums[idx] = nums2[j]
            j += 1; idx += 1
        return nums[(sz - 1) / 2] if sz % 2 == 1 else (nums[(sz - 1) / 2] + nums[(sz - 1) / 2 + 1]) * 0.5


    # @param heights: a list of integers
    # @return: a integer
    def trapRainWater(self, heights):
        if not heights or len(heights) < 3:
            return 0

        sz = len(heights)
        leftmax, rightmax = [0] * sz, [0] * sz
        leftmax[0], rightmax[sz - 1] = heights[0], heights[sz - 1]
        for i in xrange(1, sz):
            leftmax[i] = max(leftmax[i - 1], heights[i])
        for i in xrange(sz - 2, 0):
            rightmax[i] = max(rightmax[i + 1], heights[i])
        ans = 0
        for i, h in enumerate(heights):
            ans += max(0, min(leftmax[i], rightmax[i]) - h)
        return ans


s = Solution()
print s.findMedianSortedArrays([], [2,3])