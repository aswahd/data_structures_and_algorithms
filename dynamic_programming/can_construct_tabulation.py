def can_construct(target_string, wordbank):
    table = [False] * (len(target_string) + 1)
    table[0] = True

    for i in range(len(target_string) + 1):

        if table[i]:  # if True
            for word in wordbank:
                len_word = len(word)
                if target_string[i:len_word+i] == word:
                    table[len_word + i] = True

    return table[len(target_string)]


print(can_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))  # True
print(can_construct("skateboard", ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))  # False
print(can_construct("enterapotentpot", ['a', 'p','ent', 'enter', 'ot', 'o', 't']))  # True
print(can_construct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef',
                    [
                        'e',
                        'ee',
                        'eee',
                        'eeee',
                        'eeeee',
                        'eeeeee'
                    ]))  # False
