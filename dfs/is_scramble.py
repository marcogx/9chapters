from counter.is_anagram import is_anagram


def is_scramble(s1, s2):
    l1, l2 = len(s1), len(s2)
    if l1 != l2:
        return False
    if s1 == s2:
        return True
    if l1 == 1:
        return False
    # Very important pruning !! Use O(l1 + l2) to avoid exponential dfs
    if not is_anagram(s1, s2):
        return False

    for i in xrange(l1 - 1):
        s11, s12 = s1[0:i + 1], s1[i + 1:l1]
        s21, s22 = s2[0:i + 1], s2[i + 1:l1]
        if is_scramble(s11, s21) and is_scramble(s12, s22):
            return True
        s21, s22 = s2[0:l1 - i - 1], s2[l1 - i - 1:l1]
        if is_scramble(s11, s22) and is_scramble(s12, s21):
            return True
    return False