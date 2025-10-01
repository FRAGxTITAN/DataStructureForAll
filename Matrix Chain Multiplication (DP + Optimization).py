def matrix_chain_order(p):
    n = len(p) - 1
    dp = [[0] * n for _ in range(n)]

    for l in range(2, n+1):  # chain length
        for i in range(n-l+1):
            j = i+l-1
            dp[i][j] = float("inf")
            for k in range(i, j):
                q = dp[i][k] + dp[k+1][j] + p[i]*p[k+1]*p[j+1]
                dp[i][j] = min(dp[i][j], q)

    return dp[0][n-1]


# Example
arr = [1, 2, 3, 4, 3]
print("Minimum multiplications:", matrix_chain_order(arr))
