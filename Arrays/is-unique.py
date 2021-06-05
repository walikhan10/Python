# Determine whether or not a given string contains no duplicate characters.

def isDupi(str):

    for i in range(len(str)):
        for j in range(i + 1, len(str)):
            if(str[i] == str[j]):
                return False

    # If no duplicate characters
    # encountered, return true
    return True


# print(isDupi('aaaaaa'))
# print(isDupi('abcdefg'))
# print(isDupi(''))
# print(isDupi('abcdefghijklmnopqrstuvwxyzz'))
# print(isDupi('abcdefghijklmnopqrstuvwxyz'))


def isDup_2(str):

    for i in range(len(str)):
        for j in range(i+1, len(str)):
            if str[j] == str[i]:
                return False
    return True


print(isDup_2('abcdefghijklmnopqrstuvwxyz'))
