def calculate(s: str) -> int:
    stack = []
    res = 0
    curr = 0

    def process(st):
        result = st.pop(0)
        while st:
            si, v = st.pop(0), st.pop(0)
            if si == '+':
                result += v
            else:
                result -= v
        return result

    for c in s:
        if c == ' ':
            continue

        if c.isdigit():
            curr = curr * 10 + int(c)
        if c in {'-', '+', '(', ')'}:
            if curr != 0:
                stack.append(curr)
                curr = 0
        if c in {'-', '+', '('}:
            stack.append(c)
        if c == ')':
            temp = []
            while stack[-1] != '(':
                temp.append(stack.pop())
            r = process(temp)

            stack.pop()
            stack.append(r)

    if curr:
        stack.append(curr)

    return process(stack)

print(calculate(
" 2-1 + 2 "))
