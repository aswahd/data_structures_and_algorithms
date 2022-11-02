def can_construct(target_string, words, memo=None):
    if memo is None:
        memo = {}
    if target_string in memo: return memo[target_string]
    if target_string == '': return True

    for word in words:
        if word == target_string[:len(word)]:
            new_target = target_string[len(word):]
            if can_construct(new_target, words, memo):
                memo[target_string] = True
                return True
    memo[target_string] = False
    return False


print(can_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))  # True
print(can_construct("skateboard", ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))  # False
print(can_construct('eeeeeeeeeeeeeeeeeeeedeeeeeeeeeeeeeeeeef',
                    [
                        'e',
                        'ee',
                        'eee',
                        'eeee',
                        'eeeee',
                        'eeeeee'
                    ]))  # False

