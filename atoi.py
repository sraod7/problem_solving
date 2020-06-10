def myAtoi(s: str) -> int:
    is_neg = False
    res = ''
    char_count = 0
    valid_nums = set([str(i) for i in range(10)])
    valid_sign = {'+', '-'}
    valid_space = ' '
    int_min = -1 * (2 ** 31)
    int_max = (2 ** 31) - 1

    for c in s:
        if c is valid_space and char_count == 0:
            continue
        if c in valid_nums or c in valid_sign:
            char_count += 1
            if c in valid_sign:
                if char_count == 1:
                    is_neg = True if c == '-' else False
                else:
                    break
            if c in valid_nums:
                res += c
            continue
        break

    if res == '':
        return 0

    res = int(res)
    res = -1 * res if is_neg else res

    if res > int_max:
        return int_max

    if res < int_min:
        return int_min

    return res

print(myAtoi('   -42'))