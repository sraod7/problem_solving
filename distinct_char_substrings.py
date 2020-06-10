def countLetters(S: str) -> int:
    res = len(set(S))
    last_char = None

    for c in S:
        if not last_char:
            last_char = c
        elif last_char == c:
            res += 1
        elif last_char != c:
            last_char = c

    return res

print(countLetters('aaaba'))