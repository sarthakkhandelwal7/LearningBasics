def find_path(m: int, n: int, dp):
    if n == 0 or m == 0:
        return 1
    dp[m][n] += find_path(m - 1, n, dp) if dp[m - 1][n] == 0 else dp[m - 1][n]
    dp[m][n] += find_path(m, n - 1, dp) if dp[m][n - 1] == 0 else dp[m][n - 1]
    return dp[m][n]


if __name__ == '__main__':
    m = 3
    n = 2
    dp = [[0 for _ in range(n)] for _ in range(m)]
    print(find_path(m - 1, n - 1, dp))
