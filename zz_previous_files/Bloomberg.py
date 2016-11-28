#merge two sorted arrays

2399  
145



class Solution(object):
	def lengthOfLongestSubstringTwoDistinct(self, s):
		"""
        :type s: str
        :rtype: int
        """
		if not s:
			return 0
		ans, start, i, count, map = 0, 0, 0, 0, {}
		while i < len(s):
			if s[i] not in map or map[s[i]] < start:
				count += 1
				map[s[i]] = i
			if count > 2:
				ans = max(ans, i - start)
				j = i - 1
				while j >= 1 and s[j] == s[j - 1]:
					j -= 1
				start = j
				count -= 1
			i += 1

		ans = max(ans, i - start)
		return ans


def main():
	s = Solution()
	print s.lengthOfLongestSubstringTwoDistinct('abccbbcccaaacaca')


if __name__ == '__main__':
	main()
