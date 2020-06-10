def knapsack_bf(ws, ps, c):
    """ws -> weights and ps -> profits and c -> capacity"""
    res = []
    for i in range(len(ws)):
        for j in range(i + 1, len(ws)):
            if ws[i] + ws[j] <= c:
                res.append([i, j, ws[i], ws[j], ps[i] + ps[j]])

    res.sort(key=lambda x: -x[4])

    return res[0]


print(knapsack_bf([1,2,3,5], [1,6,10,16], 7))

def knapsack_re(ws, ps, c, i):
    if i > len(ws):
        return 0
    if i == len(ws):
        return ps[i]

    p1 =  ps