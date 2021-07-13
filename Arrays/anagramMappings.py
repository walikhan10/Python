

def anagramMappings(nums1, nums2):

    dict = {}
    index = 0
    output = []
    for i in nums2:
        if i not in dict:
            dict[i] = index
            index += 1
        else:
            dict[i] = index
            index += 1

    for j in nums1:
        if j in dict:
            output.append(dict[j])

    return output


print(anagramMappings([84, 8, 0, 84, 0, 84], [84, 84, 8, 0, 0, 84]))
