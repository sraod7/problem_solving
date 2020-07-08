
def strStr(haystack: str, needle: str) -> int:
    base = 26
    hash_n = 0
    hash_h = 0
    curr = []
    for i in range(len(needle)):
        hash_n += ord(needle[i]) * (base ** i)
        hash_h += ord(haystack[i]) * (base ** i)
        curr.append(haystack[i])

    if hash_n == hash_h:
        return 0

    for i in range(len(needle), len(haystack)):
        hash_h -= ord(curr[0])
        hash_h = int(hash_h / base)
        hash_h += ord(haystack[i]) * (base ** (len(needle) - 1))
        curr.pop(0)
        curr.append(haystack[i])
        if hash_h == hash_n:
            return i - len(needle) + 1

    return -1

print(strStr('hello', 'll'))