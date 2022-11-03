def all_construct(target_string, wordbank):
    table = [[] for _ in range(len(target_string) + 1)]
    table[0] = [[]]
    for i in range(len(target_string) + 1):
        if table[i]:
            for word in wordbank:
                len_word = len(word)
                if word == target_string[i: i + len_word]:
                    new_combination = [p + [word] for p in table[i]]  # insert word to each existing path
                    table[i + len_word].extend(new_combination)
    return table[-1]


print(all_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd', 'ef', 'c']))
print(all_construct('purple', ['purp', 'p', 'ur', 'le', 'purpl']))
print(all_construct('aaaaaaf',
                    ['a', 'aa', 'aaa', 'aaaa', 'aaaaa']))  # []
