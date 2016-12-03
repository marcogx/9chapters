# Given an array of meeting time intervals consisting
# of start and end times [[s1,e1],[s2,e2],...] (si < ei),
# find the minimum number of conference rooms required.


def min_meeting_rooms(intervals):
    if not intervals:
        return 0

    points = []
    # use 0/1 to indicate left/right to break tie
    for i in intervals:
        points.append((i.start, 1))
        points.append((i.end, 0))
    points.sort()

    count, res = 0, 0
    for p in points:
        if p[1] == 1:
            count += 1
            res = max(res, count)
        else:
            count -= 1

    return res