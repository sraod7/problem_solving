def numSquares(n):
    squares = [i ** 2 for i in range(1, int(n**.5) + 1)]
    dp = [float('inf')] * (n + 1)
    dp[0] = 0

    for i in range(1, len(dp)):
        for square in squares:
            if square > i:
                break

            dp[i] = min(dp[i], 1 + dp[i - square])

    return dp[n]

print(numSquares(1))

