class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for val in s:
            if val in pairs and stack:
                last_insert = stack.pop()
                if pairs[val] != last_insert:
                    return False
            else:
                stack.append(val)

        return len(stack) == 0