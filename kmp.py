def lps_array(pattern, M, lps):
    len = 0
    i = 1
    while i < M:
        if pattern[i] == pattern[len]:
            len += 1
            lps[i] = len
            i += 1
        else:

            if len != 0:
                len = lps[len - 1]

            else:
                lps[i] = 0
                i += 1


def kmp_search_in_string(pattern, txt):
    M = len(pattern)
    N = len(txt)
    increment = 0
    lps = [0] * M
    j = 0
    lps_array(pattern, M, lps)
    print(lps)

    i = 0
    while i < N:
        increment += 1
        if pattern[j] == txt[i]:
            i += 1
            j += 1

        if j == M:
            print("Found pattern at index " + str(i - j) + "-" + str(i - j + M - 1))
            j = lps[j - 1]

        elif pattern[j] != txt[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    print(increment)


if __name__ == '__main__':
    pattern = "A"
    txt = "AAQADAA"

    kmp_search_in_string(pattern, txt)
