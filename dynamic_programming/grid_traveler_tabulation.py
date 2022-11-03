def grid_traveler(m, n):
    table = [[0 for _ in range(n+1)] for _ in range(m + 1)]
    table[1][1] = 1     # base case
    for i in range(m + 1):
        for j in range(n + 1):
            if (i + 1) <= m:
                table[i + 1][j] += table[i][j]
            if (j + 1) <= n:
                table[i][j + 1] += table[i][j]
    return table[m][n]


print(grid_traveler(1, 1))    # 1
print(grid_traveler(2, 3))    # 3
print(grid_traveler(3, 2))    # 3
print(grid_traveler(3, 3))    # 6
print(grid_traveler(18, 18))  # 2333606220
