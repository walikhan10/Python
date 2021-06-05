

def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


def twoSums_sorted(nums, target):

    l = 0
    r = len(nums) - 1

    while r > l:

        curr = nums[l] + nums[r]

        if curr < target:
            l += 1
        elif curr > target:
            r -= 1

        else:
            return [nums[l], nums[r]]

    return[-1, 1]


nums1 = [2, 7, 11, 15]
target1 = 9


print(twoSums(nums1, target1))
