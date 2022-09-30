def isValidSubsequence(array, sequence):
    last_idx = 0
    for i in range(len(sequence)):

        for j in range(last_idx, len(array)):

            if sequence[i] == array[j]:
                last_idx = j + 1
                break
        else:
            return False

    return True


if __name__ == "__main__":
    array = [5, 1, 22, 25, 6, -1, 8, 10]
    sequence = [1, 6, -1, 10]

    print(isValidSubsequence(array, sequence))

