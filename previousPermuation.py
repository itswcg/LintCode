class Solution:
    """
    @param: nums: A list of integers
    @return: A list of integers that's previous permuation
    """

    def previousPermuation(self, nums):
        if len(nums) <= 1:
            return nums
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] > nums[i + 1]:
                for j in range(len(nums) - 1, -1, -1):
                    if nums[j] < nums[i]:
                        nums[j], nums[i] = nums[i], nums[j]
                        nums[i + 1:] = reversed(nums[i + 1:])
                        break
                break
            if i == 0:
                nums.reverse()
        return nums
