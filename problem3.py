alphabet = string.ascii_letters

# Iteration
def isPalindromeIter(s):
    s = s.lowercase
    i, j = 0, len(s) - 1
    while i < j:
        if s[i] not in alphabet:
            i += 1
            continue
        if s[j] not in alphabet:
            j -= 1
            continue
        if s[i] != s[j]:
            return False
        i, j = i+1, j-1
    return True

# Recursion
def isPalindromeRecur(s):
    s = s.lowercase
    if not len(s):
        return True
    i, j = 0, len(s) - 1
    while s[i] not in alphabet:
        i += 1
    while s[j] not in alphabet:
        j -= 1
    if s[i] != s[j]:
        return False

    i += 1
    j -= 1
    substring = s.substring(i,j)
    return isPalindromeRecur(substring)
