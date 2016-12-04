from prime import first_n_primes


class Solution(object):
    def __init__(self):
        self.primes = first_n_primes.first_n_primes(26)

    def groupAnagrams(self, strs):
        if not strs:
            return []

        map = {}
        for s in strs:
            k = self.key(s)
            if k in map:
                map[k].append(s)
            else:
                map[k] = [s]

        return map.values()

    # def key(self, s):
    #     return ''.join(sorted(s))

    def key(self, s):
        code, primes = 1, self.primes
        for c in s:
            code *= primes[ord(c) - 97]
        return code


def main():
    print Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])


if __name__ == '__main__':
    main()