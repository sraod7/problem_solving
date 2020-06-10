from typing import List


def removeCoveredIntervals( intervals: List[List[int]]) -> int:
    res = []
    for inter in intervals:
        if not res:
            res.append(inter)
        else:
            f = False
            for r in res:
                if r[0] <= inter[0] and r[1] <= inter[1]:
                    f = True
                    break
            if not f:
                res.append(inter)

    return len(res)

print(removeCoveredIntervals([[1,4],[3,6],[2,8]]))
