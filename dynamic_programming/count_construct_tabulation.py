def count_construct(target_string, wordbank):
    table = [0] * (len(target_string) + 1)
    table[0] = 1
    for i in range(len(target_string) + 1):
        for word in wordbank:
            len_word = len(word)
            if word == target_string[i: i + len_word]:
                table[i + len_word] += table[i]

    return table[-1]


print(count_construct('purple', ['purp', 'p', 'ur', 'le', 'purpl']))  # 2
print(count_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))  # 1
print(count_construct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))  # 0
print(count_construct('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't']))  # 4
print(count_construct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeef',
                      [
                          'e',
                          'ee',
                          'eee',
                          'eeee',
                          'eeee'
                      ]))  # 0
