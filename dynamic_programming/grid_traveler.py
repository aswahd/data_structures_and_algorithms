def grid_traveler(rows, cols, memo=None):
    if memo is None: memo = {}
    if rows == 0 or cols == 0:
        return 0
    if rows == cols == 1:
        return 1
    if (rows, cols) in memo or (cols, rows) in memo:
        try:
            return memo[(rows, cols)]
        except KeyError:
            return memo[(cols, rows)]
    # Go down, Go right
    memo[(rows, cols)] = grid_traveler(rows - 1, cols, memo) + \
                         grid_traveler(rows, cols - 1, memo)
    return memo[(rows, cols)]


print(grid_traveler(2, 2))

