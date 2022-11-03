def best_sum(target_sum, numbers):
    table = [None] * (target_sum + 1)
    table[0] = []

    for i in range(target_sum + 1):
        if table[i] is not None:
            for num in numbers:
                if (i + num) <= target_sum:
                    path = [n for n in table[i]] + [num]   # copy list
                    if table[i + num] is None or len(path) < len(table[i + num]):
                        table[i + num] = path
    return table[target_sum]


print(best_sum(7, [5, 3, 4, 7]))     # [7]
print(best_sum(8, [2, 3, 5]))        # [3, 5]
print(best_sum(8, [1, 4, 5]))        # [4, 4]
print(best_sum(100, [1, 2, 5, 25]))  # [25, 25, 25, 25]
