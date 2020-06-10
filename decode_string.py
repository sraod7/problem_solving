def decodeString(s: str) -> str:
    mult = 0
    curr_str = ''
    stack = []

    for c in s:
        if c.isdigit():
            mult = mult * 10 + int(c)
        if c.isalpha():
            curr_str += c
        if c == '[':
            stack.append(curr_str)
            stack.append(mult)
            mult = 0
            curr_str = ''
        if c == ']':
            num_ = stack.pop()
            str_ = stack.pop()

            curr_str = str_ + num_ * curr_str

    return curr_str

print(decodeString("2[abc]3[cd]ef"))