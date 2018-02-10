class Solution:
    """
    @param: nums: an array containing n + 1 integers which is between 1 and n
    @return: the duplicate one
    """

    def findDuplicate(self, nums):
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return nums[i]
