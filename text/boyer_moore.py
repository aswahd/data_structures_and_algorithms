
def boyer_moore(T, P):

    n, m = len(T), len(P)
    i = k = m - 1
    last = {}
    for i, c in enumerate(P):
        last[c] = i

    while i < n:

        if T[i] == P[k]:
            if k == 0:
                return i
            i -= 1
            k -= 1
        else:
            j = last.get(T[i], -1)
            i += m - min(k, j + 1)

            k = m - 1

    return -1


if __name__ == "__main__":
    text = "hello boyer-moore"
    pattern = "boyer-moore"
    print(text.find(pattern))
    print(boyer_moore(text, pattern))
