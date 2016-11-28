# https://leetcode.com/problems/find-all-anagrams-in-a-string/


class Solution(object):
    def findAnagrams(self, s, p):
        if not s or not p or len(s) < len(p):
            return []

        res = []
        smap, pmap = {}, {}
        slen, plen = len(s), len(p)
        for c in p:
            pmap[c] = pmap.get(c, 0) + 1

        for i in xrange(slen):
            smap[s[i]] = smap.get(s[i], 0) + 1
            if i >= plen:
                smap[s[i - plen]] -= 1
                if smap[s[i - plen]] == 0:
                    del smap[s[i - plen]]
            if smap == pmap:
                res.append(i - plen + 1)

        return res


solution = Solution()
print solution.findAnagrams("cbaebabacd", "abc")
print solution.findAnagrams("cbaebabacd", "a")
