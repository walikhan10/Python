

# my first attempt


def rev_string(s):

    i = len(s)-1
    s2 = ""

    while i >= 0:
        s2 += s[i]
        i -= 1
    return list(s2)


test = ["y", "e", "l", "l", "o"]


print(rev_string(test))
