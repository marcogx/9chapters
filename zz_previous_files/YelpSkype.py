def score_possible_anytime(scores, candi):
    if candi == 0:
        return True
    if not scores or scores[0] > candi:
        return False
    scores = sorted(set(scores))
    possible = [False]
    dfs1(possible, scores, 0, candi)
    return possible[0]


def dfs1(possible, scores, start, candi):
    if candi == 0:
        possible[0] = True
        return
    for i in xrange(start, len(scores)):
        if possible[0] or scores[i] > candi:
            break
        dfs1(possible, scores, i, candi - scores[i])


def score_possible_onetime(scores, candi):
    if candi == 0:
        return True
    if not scores or scores[0] > candi:
        return False
    scores.sort()
    possible = [False]
    dfs2(possible, scores, 0, candi)
    return possible[0]


def dfs2(possible, scores, start, candi):
    if candi == 0:
        possible[0] = True
        return
    for i in xrange(start, len(scores)):
        if possible[0] or scores[i] > candi:
            break
        dfs2(possible, scores, i + 1, candi - scores[i])



def main():
    scores = [3, 5, 5]
    candis = [2, 1, 7, 11, 13, 6, 17, 10, 15]
    for candi in candis:
        print 'any-- candi: ', candi, score_possible_anytime(scores, candi)
        print 'one-- candi: ', candi, score_possible_onetime(scores, candi)

main()
