def convert_to_binary(val):
    stack = []
    while val > 2:
        stack.append(str(val % 2))
        val = int(val / 2)
    stack.append(str(val))

    return int(''.join(stack[::-1]))


print(convert_to_binary(242))
