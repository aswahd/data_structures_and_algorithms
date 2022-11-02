def how_sum(target_sum, numbers, memo=None):
    if memo is None:
        memo = {}
    if target_sum in memo: return memo[target_sum]
    if target_sum == 0: return []
    if target_sum < 0: return None

    for num in numbers:
        new_target = target_sum - num
        return_value = how_sum(new_target, numbers, memo)
        if return_value is not None:
            return_value.append(num)
            memo[target_sum] = return_value
            return return_value
    memo[target_sum] = None
    return None


print(how_sum(7, [5, 3, 4, 7]))
print(how_sum(7, [2, 3, 1]))
print(how_sum(300, [7, 14]))
