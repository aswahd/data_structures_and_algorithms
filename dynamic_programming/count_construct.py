def count_construct(target_string, wordbank, memo=None):
    if memo is None:
        memo = {}
    if target_string in memo: return memo[target_string]
    if target_string == '': return 1

    count = 0
    for word in wordbank:
        if word == target_string[:len(word)]:
            new_target = target_string[len(word):]
            count += count_construct(new_target, wordbank, memo)
    memo[target_string] = count
    return count


print(count_construct('purple', ['purp', 'p', 'ur', 'le', 'purpl']))    # 2
print(count_construct("abcdef", ['ab', 'abc', 'cd', 'def', 'abcd']))    # 1
print(count_construct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))    # 0
print(count_construct('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 'ot']))  # 4
print(count_construct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef',
                      [
                          'e',
                          'ee',
                          'eee',
                          'eeee',
                          'eeeee'
                      ]))   # 0
