

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


nums1 = [2, 15, 11, 7]
target1 = 9


print(twoSums_sorted(nums1, target1))


def twoSum_hash(nums, target):
    prevMap = {}  # val:index
    for i, n in enumerate(nums):
        diff = target - n
        if diff in prevMap:
            return [prevMap[diff], i]
        prevMap[n] = i
