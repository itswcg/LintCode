class Solution:
    """
    @param: nums: An ineger array
    @return: An integer
    """

    def removeDuplicates(self, nums):
        n = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[n]:
                n += 1
                nums[n] = nums[i]
        del nums[n + 1: len(nums)]
        return len(nums)


print(Solution().removeDuplicates([1, 1, 2]))
