def decodeString(s: str) -> str:
    stack = []

    i = 0
    while i < len(s):
        if s[i].isdigit():
            val = 0
            while i < len(s) and s[i].isdigit():
                val = val * 10 + int(s[i])
                i += 1
            stack.append(val)

        elif s[i] == '[':
            stack.append(s[i])
            i += 1
        elif s[i].isalpha():
            str_ = ''
            while i < len(s) and s[i].isalpha():
                str_ += s[i]
                i += 1
            stack.append(str_)
        elif s[i] == ']':
            str_ = stack.pop()
            stack.pop()
            val = stack.pop()
            stack.append(str_ * val)
            i += 1

    return ''.join(stack)


print(decodeString("3[a2[c]]"))