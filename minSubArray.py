class Solution:
    """
    @param: nums: a list of integers
    @return: A integer indicate the sum of minimum subarray
    """

    def minSubArray(self, nums):
        i, sum, sum_min = 0, 0, 2147483648
        while i < len(nums):
            sum += nums[i]
            if sum < sum_min:
                sum_min = sum
            if sum > 0:
                sum = 0
            i += 1
        return sum_min


print(Solution().minSubArray([1, -1, -2, 1]))
