def isPalindrome(s: str) -> bool:
    low = 0
    high = len(s) - 1

    while low < high:
        while (not s[low].isalpha()) or (not s[low].isdigit()) and low < high:
            low += 1
        while (not s[high].isalpha()) and (not s[low].isdigit()) and low < high:
            high -= 1

        if low == high:
            return True

        if s[low].lower() != s[high].lower():
            return False

        low += 1
        high -= 1

    return True

print(isPalindrome('0P'))
