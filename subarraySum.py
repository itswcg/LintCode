class Solution:
    """
    @param: nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """

    def subarraySum(self, nums):
        for i in range(len(nums)):
            sum = nums[i]
            if sum == 0:
                return [i, i]
            for j in range(i + 1, len(nums)):
                sum += nums[j]
                if sum == 0:
                    return [i, j]
