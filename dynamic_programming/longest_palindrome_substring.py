def longest_substring(inp):
    start = end = 0
    n = len(inp)
    table = [[False for _ in range(n)] for _ in range(n)]
    for i in range(n):
        table[i][i] = True  # strings of length 1
    # Traverse from bottom-right to top-left of the upper triangle
    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            if j - i == 1:  # string of length 2
                table[i][j] = inp[i] == inp[j]
            else:
                table[i][j] = (inp[i] == inp[j]) and table[i+1][j-1]
            if (j - i > end - start) and table[i][j]:
                start, end = i, j
    return inp[start: end + 1]


text = 'some random text before the real shitin computer science, the longest palindromic substring or longest symmetric factor problem is the problem of finding a maximum-length contiguous substring of a given string that is also a palindrome..emordnilap a osla si taht gnirts nevig a fo gnirtsbus suougitnoc htgnel-mumixam a gnidnif fo melborp eht si melborp rotcaf cirtemmys tsegnol ro gnirtsbus cimordnilap tsegnol eht ,ecneics retupmoc nisome random text after the real shit'

print(len(longest_substring(text)))  # 398
