# A palindrome is a word, phrase, or sequence that reads the same backwards as forwards. e.g. madam

# Preliminary notes and ideas :

# int l = 0
# int r = len - 1

# while r > l:

# while r>l:
# l++
# r--

# if r != l:
# return false

# if r < l:
# return true

# @param s, a string
# @return a boolean
def isPalindrome(s):
    l = 0
    r = len(s) - 1

    while l < r:
        while l < r and not s[l].isalnum():
            l += 1
        while l < r and not s[r].isalnum():
            r -= 1
        if s[l].lower() != s[r].lower():
            return False
        l += 1
        r -= 1
    return True


def isPalindrome_2(s):

    l, r = 0, len(s) - 1

    while l < r:
        if not s[l].isalnum():
            l += 1
        elif not s[r].isalnum():
            r -= 1
        else:
            if s[l].lower() != s[r].lower():
                return False
            else:
                l += 1
                r -= 1
    return True


print(isPalindrome_2("racecarq"))
