

# my first attempt
# it does not account for "([)]" correctly.
# it looks over the fact that it should close properly
# Also it is not time effeicient because it is Brute Force

def valid(s):

    contain = ["{}", "[]", "()"]
    check = 0
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            pair = s[i] + s[j]
            if pair in contain:
                check += 1
    if check == len(s)/2:
        return True
    else:
        return False


print(valid('([)]'))
