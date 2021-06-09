

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


# print(valid('([)]'))


# Algorithm

# Initialize a stack S.
# Process each bracket of the expression one at a time.
# If we encounter an opening bracket, we simply push it onto the stack. This means we will process it later, let us simply move onto the sub-expression ahead.
# If we encounter a closing bracket, then we check the element on top of the stack. If the element at the top of the stack is an opening bracket of the same type, then we pop it off the stack and continue processing. Else, this implies an invalid expression.
# In the end, if we are left with a stack still having elements, then this implies an invalid expression.

def valid_stack(s):

    # if len(s) % 2 != 0:
    #     return False

    stack = []
    map = {
        ")": "(",
        "}": "{",
        "]": "["
    }

    for c in s:
        if c in map:  # closing paran
            if stack and stack[-1] == map[c]:
                stack.pop()
            else:
                return False
        else:
            stack.append(c)
    return True if not stack else False


print(valid_stack('([])'))
