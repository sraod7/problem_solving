
def calculate(s: str) -> int:
    stack = []

    i = 0

    while i < len(s):
        if s[i] == ' ':
            i += 1
            continue

        if s[i].isdigit():
            val = 0
            while i < len(s) and s[i].isdigit():
                val = val * 10 + int(s[i])
                i += 1

            if stack and stack[-1] in {'*', '/'}:
                sym = stack.pop()
                val_ = stack.pop()
                val = val_ // val if sym == '/' else val_ * val

            stack.append(val)

        elif s[i] in {'+', '-', '*', '/'}:
            stack.append(s[i])
            i += 1

    res = stack.pop(0)

    while stack:
        sym = stack.pop(0)
        val = stack.pop(0)
        res = res + val if sym == '+' else res - val

    return res

print(calculate("1+1+1"))