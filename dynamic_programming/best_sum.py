def best_sum(target_sum, numbers, memo=None):
    """ The shortest list of numbers from numbers such that they sum up to target_sum """
    if memo is None:
        memo = {}
    if target_sum in memo: return memo[target_sum]
    if target_sum < 0: return None
    if target_sum == 0: return []

    best = None
    for num in numbers:
        new_target = target_sum - num
        return_value = best_sum(new_target, numbers, memo)
        if return_value is not None:
            combination = return_value + [num]
            if best is None or (len(combination) < len(best)):
                best = combination
    memo[target_sum] = best
    return best


print(best_sum(7, [5, 3, 4, 7]))     # [7]
print(best_sum(8, [2, 3, 5]))        # [3, 5]
print(best_sum(8, [1, 4, 5]))        # [4, 4]
print(best_sum(100, [1, 2, 5, 25]))  # [25, 25, 25, 25]
