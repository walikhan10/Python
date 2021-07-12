
#not done

def romantoInt(s):

    # mapping
    roman_table = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

# you loop through the roman numeral and then add up the value
# unless the value beorei tiis smalelr then you  have to do the rule

# 123
# example: XII
# I would be 2, and start at 'I'
    N = len(s) - 1
    i = N-1
    output = 0
    while i >= 0:

        output += roman_table[s[i]]
        i -= 1

    return output


test = "III"

print(romantoInt(test))
