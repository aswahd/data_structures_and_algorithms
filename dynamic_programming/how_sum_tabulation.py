def how_sum(target_sum, numbers):
    table = [None] * (target_sum + 1)
    table[0] = []

    for i in range(target_sum + 1):
        if table[i] is not None:
            for num in numbers:
                if (i + num) <= target_sum:
                    new_path = [n for n in table[i]] + [num]   # copy list
                    table[i + num] = new_path
                    # you can return early
                    if (i + num) == target_sum:
                        return table[target_sum]
    return table[target_sum]


print(how_sum(7, [2, 3]))
print(how_sum(7, [5, 3, 4, 7]))
print(how_sum(7, [2, 4]))
print(how_sum(8, [2, 3, 5]))
print(how_sum(300, [7, 14]))
