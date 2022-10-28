def merge(s1, s2, s):
    """ Merge s1 and s2 into s """
    i = j = 0

    while i + j < len(s):
        if j == len(s2) or (i < len(s1) and s1[i] < s2[j]):
            s[i + j] = s1[i]
            i += 1
        else:
            s[i + j] = s2[j]
            j += 1


def merge_sort(s):

    if len(s) < 2:
        return s
    mid = len(s) // 2
    s1, s2 = s[:mid], s[mid:]
    merge_sort(s1)
    merge_sort(s2)
    merge(s1, s2, s)


if __name__ == "__main__":
    arr = [85, 24, 63, 45, 17, 31, 96, 50]
    merge_sort(arr)
    print(arr)
