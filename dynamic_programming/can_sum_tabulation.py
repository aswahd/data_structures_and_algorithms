def can_sum(target_sum, numbers):
    table = [False] * (target_sum + 1)
    table[0] = True

    for i in range(target_sum + 1):
        if table[i]: continue
        for num in numbers:
            if i + num <= target_sum:
                table[i + num] = True    # can generate i + num
                if table[target_sum]:
                    return True
    return False


print(can_sum(7, [2, 3]))        # True
print(can_sum(3, [2]))           # False
print(can_sum(7, [5, 3, 4, 7]))  # True
print(can_sum(7, [2, 4]))        # False
print(can_sum(8, [2, 3, 5]))     # True
print(can_sum(300, [7, 14]))     # False
