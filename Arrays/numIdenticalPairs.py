
def numIdenticalPairs(nums):

    output = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j] and i < j:
                output += 1
    return output


def numIdenticalPairs2(nums):

    result = 0
    dict = {}

    for i in nums:
        if i in dict:
            result += dict[i]
            dict[i] + 1
        else:
            dict[i] += 1

    return result


test = [1, 2, 3, 1, 1, 3]

numIdenticalPairs2(test)


# class Solution:
#     def numIdenticalPairs(self, nums: List[int]) -> int:
#         my_count = 0
#         my_dict = {}

#         for n in nums:
#             # Check to see if number has already been encountered
#             if n in my_dict:
#                 # Increase count by the number of previous instances
#                 my_count += my_dict[n]

#                 # Increase the count of previous observation
#                 my_dict[n] += 1
#             else:
#                 # Store newly encountered number along with its count
#                 my_dict[n] = 1

#         return my_count
