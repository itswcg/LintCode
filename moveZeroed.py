class Solution:
    """
    @param: nums: an integer array
    @return:
    """

    def moveZeroes(self, nums):
        for num in nums:
            if num == 0:
                nums.remove(num)
                nums.append(0)
        return nums


print(Solution().moveZeroes([0, 1, 0, 3, 12]))
