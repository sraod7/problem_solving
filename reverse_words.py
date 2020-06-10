def reverseWords(s: str) -> str:
    return ' '.join([val.strip() for val in s.split(' ') if val != ''][::-1])

print(reverseWords("a good   example"))

