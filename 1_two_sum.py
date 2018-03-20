# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# Example:
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

def twoSum(nums,target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    since we may not use the same element twice, so at most we could loop the list one time.
    foreach element we need to know if there is another element exist in the list can sum up to target.
    we can't have the second loop to sum therefor each element will be use n-1 times.
    so we switch to use a Dict which the key is the element itself,and value is the index.
    and we just need to check if the dict contains the key(target -nums[i]).
    """
    dict = {}
    for index in range(len(nums)):
        if target - nums[index] in dict:
            perv = dict[target - nums[index]]
            return [perv,index]
        else:
            dict[nums[index]] = index

print(twoSum([2,7,11,15],9))
