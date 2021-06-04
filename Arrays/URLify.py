

def URLify(str):

    url = " "

    for i in str:
        if i == " ":
            url += "%20"
        else:
            url += i
    return url


print(URLify('Wali Khan'))


def URLify2(str):

    url = " "

    for i in str:
        if i == " ":
            url += '%20'
        else:
            url += i
    return url


print(URLify2('Wali Khan'))
