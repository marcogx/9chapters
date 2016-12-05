from collections import deque
import string


def word_ladder_lists(begin_word, end_word, word_list):
    if begin_word == end_word:
        return [[begin_word]]

    graph = build_graph(begin_word, end_word, word_list)
    if not graph:
        return []

    path, res_list = [end_word], []
    dfs(path, res_list, graph, begin_word)
    return res_list


def dfs(path, resList, graph, beginWord):
    if path[-1] == beginWord:
        resList.append(list(reversed(path)))
        return
    for nb in graph.get(path[-1], []):
        path.append(nb)
        dfs(path, resList, graph, beginWord)
        path.pop()


def build_graph(begin_word, end_word, word_list):
    word_list.add(begin_word)
    word_list.add(end_word)
    graph, queue = {}, deque()
    queue.append(end_word)
    word_list.remove(end_word)

    while queue:
        sz = len(queue)
        words = set()
        for _ in xrange(sz):
            cur = queue.popleft()
            if cur == begin_word:
                return graph

            graph[cur] = []

            for i in xrange(len(cur)):
                for c in string.lowercase:
                    word = cur[:i] + c + cur[i + 1:]
                    if word not in graph and word in word_list:
                        graph[cur].append(word)
                        words.add(word)

        for word in words:
            queue.append(word)
            word_list.remove(word)

    return {}


def main():
    s = {"hot", "cog", "dog", "tot", "hog", "hop", "pot", "dot"}
    print word_ladder_lists("hot", "dog", s)


if __name__ == '__main__':
    main()