def calPoints(ops) -> int:
    stack = []

    for val in ops:
        if val == 'C':
            stack.pop()
        elif val == '+':
            stack.append(stack[-1] + stack[-2])
        elif val == 'D':
            stack.append(stack[-1] * 2)
        else:
            stack.append(int(val))

    return sum(stack)

print(calPoints(["5","-2","4","C","D","9","+","+"]))