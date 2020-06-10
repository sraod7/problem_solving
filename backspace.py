import itertools


def backspaceCompare(S, T):
    def F(S):
        skip = 0
        for x in reversed(S):
            if x == '#':
                skip += 1
            elif skip:
                skip -= 1
            else:
                yield x

    return all([a == b for a, b in zip(F(S), F(T))])

backspaceCompare(S = "a#c", T = "b")