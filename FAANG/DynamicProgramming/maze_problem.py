def grid_path(n, m):
    memo = {}

    for i in range(1, n + 1):
        memo[(i, 1)] = 1
    for j in range(1, m + 1):
        memo[(1, j)] = 1

    print(memo)

    for i in range(2, n + 1):
        for j in range(2, m + 1):
            memo[(i, j)] = memo[(i - 1, j)] + memo[i, j - 1]

    print(memo)
    return memo[(n, m)]


if __name__ == '__main__':
    print(grid_path(18, 6))
