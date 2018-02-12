class Solution:
    """
    @param: nums: An array of integers
    @return: nothing
    """

# 倒序找递増，然后在递增中找大于i的，替换，剩下的排序

    def nextPermutation(self, nums):
        if len(nums) <= 1:
            return nums
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                for j in range(len(nums) - 1, -1, -1):
                    if nums[j] > nums[i]:
                        nums[j], nums[i] = nums[i], nums[j]
                        nums[i + 1:] = sorted(nums[i + 1:])
                        break
                break
            else:
                if i == 0:
                    nums.sort()
        return nums
