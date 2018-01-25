class Solution:
    """
    @param: nums: A list of integers
    @return: A integer indicate the sum of max subarray
    """

    def maxSubArray(self, nums):
        i, sum, sum_max = 0, 0, -2147483648
        while i < len(nums):
            sum += nums[i]
            if sum > sum_max:
                sum_max = sum
            if sum < 0:  # 贪心算法，如果是负数，加下一个值小下个值，直接从零开始
                sum = 0
            i += 1
        return sum_max


print(Solution().maxSubArray([-2, 2, -3, 4, -1, 2, 1, -5, 3]))
