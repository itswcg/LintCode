class Solution:
    """
    @param: nums: an array of integers
    @return: nothing
    """

    def partitionArray(self, nums):
        i = 0
        j = len(nums) - 1
        while i < j:
            if nums[i] % 2 == 0 and nums[j] % 2 == 1:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
            else:
                if nums[i] % 2 == 1:
                    i += 1
                if nums[j] % 2 == 0:
                    j -= 1
