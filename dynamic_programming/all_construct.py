def all_construct(target_string, wordbank, memo=None):
    if memo is None: memo = {}
    if target_string in memo: return memo[target_string]
    if target_string == '':
        return [[]]
    all_ways_to_construct = []
    for word in wordbank:
        if word == target_string[:len(word)]:
            new_target = target_string[len(word):]
            ways_to_construct = all_construct(new_target, wordbank, memo)
            for way in ways_to_construct:
                way.insert(0, word)
            all_ways_to_construct.extend(ways_to_construct)
    memo[target_string] = all_ways_to_construct
    return all_ways_to_construct


print(all_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd', 'ef', 'c']))
print(all_construct('purple', ['purp', 'p', 'ur', 'le', 'purpl']))
print(all_construct('aaaaaaaaaaaaaaaaaaaaaaaaaaaaz',
                    ['a', 'aa', 'aaa', 'aaaa', 'aaaaa']))  # []
