from collections import deque
import string


def word_ladder_min_len(begin_word, end_word, word_list):
    # input check
    if begin_word == end_word:
        return 1

    queue, res, chars = deque(), 1, string.lowercase
    queue.append(end_word)
    if end_word in word_list:
        word_list.remove(end_word)

    while queue:
        sz = len(queue)
        for _ in xrange(sz):
            cur = queue.popleft()
            if cur == begin_word:
                return res
            for i in xrange(len(cur)):
                for c in chars:
                    word = cur[:i] + c + cur[i + 1:]
                    if word in word_list:
                        queue.append(word)
                        word_list.remove(word)
        res += 1

    return 0