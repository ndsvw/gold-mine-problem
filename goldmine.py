def goldmine(M):
    n = len(M)
    m = len(M[0])

    dp = [[None for _ in range(m)] for _ in range(n)]

    for j in range(m):
        for i in range(n):
            if j == 0:
                dp[i][j] = M[i][j]
            else:
                mx = dp[i][j-1]
                if i-1 >= 0:
                    mx = max(mx, dp[i-1][j-1])
                if i+1 < n:
                    mx = max(mx, dp[i+1][j-1])
                dp[i][j] = mx + M[i][j]

    return max([r[-1] for r in dp])


if __name__ == "__main__":
    M1 = [
        [1, 3, 1, 5],
        [2, 2, 4, 1],
        [5, 0, 2, 3],
        [0, 6, 1, 2]
    ]

    M2 = [
        [1, 3, 3],
        [2, 1, 4],
        [0, 6, 4]
    ]

    print(goldmine(M1))
    print(goldmine(M2))
