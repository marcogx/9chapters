class Solution(object):
	
	def reverse_words(self, s):
		chars = list(s)
		self.reverse_words2(chars)
		return ''.join(chars)

	def reverse_words2(self, s):
		if not s:
			return
		self.reverse_array(s, 0, len(s) - 1)
		start = 0
		for i in xrange(len(s)):
			if s[i] == ' ':
				self.reverse(s, start, i - 1)
				start = i + 1
			elif i == len(s) - 1:
				self.reverse(s, start, i)

				# while start < len(s):
				#     end = start
				#     while end < len(s) and s[end] != ' ':
				#         end += 1
				#     self.reverse_array(s, start, end - 1)
				#     start = end + 1

	def reverse_array(self, arr, i, j):
		start, end = i, j
		while start < end:
			arr[start], arr[end] = arr[end], arr[start]
			start += 1
			end -= 1

	def searchMatrix(self, matrix, target):
		"""
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
		if not matrix or not matrix[0]:
			return False
		first_col = [row[0] for row in matrix]
		temp = self.binary_search(first_col, target)
		if temp[0]:
			return True
		else:
			return self.binary_search(matrix[temp[1]], target)[0]

	# return (is_found, last idx <= target)
	def binary_search(self, arr, target):
		start, end = 0, len(arr) - 1
		while start + 1 < end:
			mid = start + (end - start) / 2
			if arr[mid] < target:
				start = mid
			elif arr[mid] > target:
				end = mid
			else:
				return (True, mid)

		if arr[start] == target:
			return (True, start)
		elif arr[end] == target:
			return (True, end)
		else:
			return (False, start)

	def merge_2_sorted_arrays(self, a, b):
		pass

	def text_sim(self, txt1, txt2):
		map1, map2 = {}, {}
		for w in txt1.split():
			map1[w] = map1.get(w, 0) + 1
			map2[w] = 0
		for w in txt2.split():
			map2[w] = map2.get(w, 0) + 1
			map1[w] = map1.get(w, 0)

		return self.cosine_sim(map1.values(), map2.values())

	def cosine_sim(self, v1, v2):
		if not v1 or not v2:
			return 2.0
		n1, n2 = self.norm(v1), self.norm(v2)
		if 0 in (n1, n2):
			return 2.0

		product = 0
		for i in xrange(len(v1)):
			product += v1[i] * v2[i]
		result = product * 1.0 / (n1 * n2)

		return float('%.4f' % result)

	def norm(self, v):
		s = 0
		for num in v:
			s += num ** 2
		return s ** 0.5

	def searchMatrix(self, matrix, target):
		"""
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
		if not matrix or not matrix[0]:
			return False
		first_col = [row[0] for row in matrix]
		temp = self.binary_search(first_col, target)
		if temp[0]:
			return True
		else:
			return self.binary_search(matrix[temp[1]], target)[0]

	# return (is_found, last idx <= target)
	def binary_search(self, arr, target):
		start, end = 0, len(arr) - 1
		while start + 1 < end:
			mid = start + (end - start) / 2
			if arr[mid] < target:
				start = mid
			elif arr[mid] > target:
				end = mid
			else:
				return (True, mid)

		if arr[start] == target:
			return (True, start)
		elif arr[end] == target:
			return (True, end)
		else:
			return (False, start)

	def min_currency(self, denos, target):
		if min(denos) > target:
			return 0
		dp = [float('inf')] * (target + 1)
		dp[0] = 0
		for d in denos:
			dp[d] = 1

		for i in xrange(1, target + 1):
			for d in denos:
				if i - d >= 0:
					dp[i] = min(dp[i], dp[d] + dp[i - d])

		return 0 if dp[-1] == float('inf') else dp[-1]

	def is_square(self, points):
		if not points:
			return False
		a = points[0]
		rest = [(self.distance(points[i], a), points[i]) for i in xrange(1, 4)]
		rest.sort()
		ac_eq_bd = self.distance(a, rest[2][1]) == self.distance(rest[0][1], rest[1][1])
		ab_eq_ad = self.distance(a, rest[0][1]) == self.distance(a, rest[1][1])
		cb_eq_cd = self.distance(rest[2][1], rest[0][1]) == self.distance(rest[2][1], rest[1][1])
		ab_eq_cb = self.distance(a, rest[0][1]) == self.distance(rest[0][1], rest[2][1])
		return ac_eq_bd and ab_eq_ad and cb_eq_cd and ab_eq_cb

	def distance(self, p1, p2):
		return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5

	def remove_dup(self, arr):
		arr.sort()



def main():
	s = Solution()
	# print s.cosine_sim([0,0,0], [2,3,4])
	# t1 = 'Julie loves me more than Linda loves me'
	# t2 = 'Jane likes me more than Julie loves me'
	# print s.text_sim(t1, t2)
	# print s.min_currency([1, 2], 3)
	# print s.min_currency([1, 2, 5, 10], 14)
	# print s.is_square([(1,1),(1,-1),(-1,1),(-1,-1)])
	# print s.is_square([(1,1),(1,-1),(-1,1),(-1,-2)])
	# print s.is_square([(0,1),(0,-1),(-1,0),(1,0)])
	# print s.is_square([(0,1),(0,-1),(-1,0),(1,1.1)])
	print s.reverse_words('the sky is blue')


if __name__ == '__main__':
	main()
