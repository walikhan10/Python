

# my first attempt


def rev_string(s):

    i = len(s)-1
    s2 = ""

    while i >= 0:
        s2 += s[i]
        i -= 1
    return list(s2)


#test = ["y", "e", "l", "l", "o"]


# print(rev_string(test))


def rev_string2(s):

    l = 0
    r = len(s)-1

    while l < r:

        # s[l], s[r] = s[r], s[l]
        # l += 1
        # r -= 1

        temp = s[l]
        s[l] = s[r]
        s[r] = temp

        l += 1
        r -= 1

    return s


test = ["h", "e", "l", "l", "o"]

print(rev_string2(test))


def reverseString(s):
    """
    :type s: str
    :rtype: str
    """
    string = list(s)
    i, j = 0, len(string) - 1
    while i < j:
        string[i], string[j] = string[j], string[i]
        i += 1
        j -= 1
    return "".join(string)


# test = ["y", "e", "l", "l", "o"]
# print(reverseString(test))
