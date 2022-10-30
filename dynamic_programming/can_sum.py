def can_sum(target_sum, numbers, memo=None):
    if memo is None:
        # Refer to https://bit.ly/mutable_default
        memo = {}
    if target_sum in memo: return memo[target_sum]
    if target_sum < 0: return False
    if target_sum == 0: return True
    for num in numbers:
        remainder = target_sum - num
        if can_sum(remainder, numbers, memo):
            memo[target_sum] = True
            return True
    memo[target_sum] = False
    return False


if __name__ == "__main__":
    print(can_sum(7, [2, 3]))        # True
    print(can_sum(3, [2]))           # False
    print(can_sum(7, [5, 3, 4, 7]))  # True
    print(can_sum(7, [2, 4]))        # False
    print(can_sum(8, [2, 3, 5]))     # True
    print(can_sum(300, [7, 14]))     # False
