def freqAlphabets(s: str) -> str:
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    map_1 = {}
    map_2 = {}

    for i in range(len(alpha)):
        if i <= 8:
            map_1[str(i + 1)] = alpha[i]
        else:
            map_2[str(i + 1) + '#'] = alpha[i]

    for k, v in map_2.items():
        if k in s:
            s = s.replace(k, v)

    for k, v in map_1.items():
        if k in s:
            s = s.replace(k, v)

    return s

print(freqAlphabets("10#11#12"))