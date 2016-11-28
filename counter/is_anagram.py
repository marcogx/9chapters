def is_anagram(s, t):
    if None in (s, t) or len(s) != len(t):
        return False

    counts, a = [0] * 26, ord('a')
    for c in s:
        counts[ord(c) - a] += 1
    for c in t:
        counts[ord(c) - a] -= 1
        if counts[ord(c) - a] < 0:
            return False

    return True