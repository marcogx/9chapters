class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return a list of lists of string
    def findLadders(self, start, end, dict):
        if not dict:
            return []
        if start == end:
            return [[start]]

        graph, level = self.bfs(start, end, dict)

        if level == 0:
            return []
        print 'current graph is', graph


        rst, words = [], [start]
        self.dfs(rst, graph, start, end, words, level)
        print 'current rst is ', rst
        return rst


    def dfs(self, rst, graph, start, end, words, level):
        if level == 0:
            rst.append(words[:])
            return

        # for word in words:
        for word in words:
            for w in self.find_next_words2(word, graph[level - 1]):
                words.append(w)
                self.dfs(rst, graph, start, end, words, level - 1)
                words.pop()


    def bfs(self, start, end, dic):
        graph, cur_words, level= {}, [end], 0
        graph[level] = cur_words
        if end in dic:
            dic.remove(end)

        while cur_words:
            next_words = []
            for word in cur_words:
                next = self.find_next_words(word, dic)
                if start in next:
                    graph[level + 1] = [start]
                    return graph, level + 1
                next_words.extend(next)
            cur_words = next_words
            level += 1
            graph[level] = cur_words

        return {}, 0

    def find_next_words(self, word, dic):
        next = []
        for i in xrange(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                new_word = word[:i] + c + word[i + 1:]
                if new_word in dic:
                    next.append(new_word)
                    dic.remove(new_word)
        return next

    def find_next_words2(self, word, dic):
        next = []
        for i in xrange(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                new_word = word[:i] + c + word[i + 1:]
                if new_word in dic:
                    next.append(new_word)
                    # dic.remove(new_word)
        return next

s = Solution()
print s.findLadders("a", "c", ["a","b","c"])
