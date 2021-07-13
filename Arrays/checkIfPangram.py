

def checkIfPangram(s):

    alpha = 'abcdefghijklmnopqrstuvwxyz'

    u = {}
    # for j in alpha:
    #     u[j] = 0

    for k in s:
        u[k] = 1

    return sum(u.values()) == 26


test = "leetcode"

print(checkIfPangram(test))
