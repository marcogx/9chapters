def merge_overlap_intervals(intervals):
    if not intervals:
        return []

    intervals.sort(key=lambda inter: inter.start)

    res = []
    for i in intervals:
        if not res or res[-1].end < i.start:
            res.append(i)
        else:
            res[-1].end = max(res[-1].end, i.end)

    return res
