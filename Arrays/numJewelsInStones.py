
def numJewelsInStones(J, S):

    dict = {}
    count = 0

    for j in J:
        if j in dict:
            dict[j] += 1
        else:
            dict[j] = 1
    for s in S:
        if s in dict:
            count += 1
    return(count)


print(numJewelsInStones("aA", "aAAbbbb"))
