def find_common(l1, l2):
    res = []
    for val in l1:
        if val in l2:
            res.append(val)

    return res


def package(arr):
    map_ = {}
    for val in arr:
        if val[0] in map_:
            map_[val[0]].append(val[1])
        else:
            map_[val[0]] = [val[1]]

    ks = list(map_.keys())

    res = []

    for i in range(len(ks) - 1):
        for j in range(i + 1, len(ks)):
            key = [ks[i], ks[j]]
            val = find_common(map_[ks[i]], map_[ks[j]])
            res.append([key, val])

    return res


input = [
    ["58", 'sub1'],
    ['58', 'sub2'],
    ['58', 'sub3'],
    ['25', 'sub1'],
    ['25', 'sub2'],
    ['98', 'sub3'],
    ['98', 'sub1'],
    ['98', 'sub4'],
    ["17", 'sub4']
]

print(package(input))

res = [
        [
            ['58', '25'], ['sub1', 'sub2']
        ],
        [
            ['58', '98'], ['sub1', 'sub3']
        ],
        [
            ['58', '17'], []
        ],
        [
            ['25', '98'], ['sub1']
        ],
        [
            ['25', '17'], []
        ],
        [
            ['98', '17'], ['sub4']
        ]
]
