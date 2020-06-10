
def romanToInt(s: str) -> int:
    one_char_map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    two_char_map = {
        'IV': 4,
        'IX': 9,
        'XL': 40,
        'XC': 90,
        'CD': 400,
        'CM': 900
    }
    res = 0
    for k, v in two_char_map.items():
        if k in s:
            res += v * s.count(k)
            s = s.replace(k, '')

    for k, v in one_char_map.items():
        if k in s:
            res += v * s.count(k)
            s = s.replace(k, '')

    return res


print(romanToInt('IV'))