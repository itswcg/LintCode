class Solution:
    """
    @param: nums: An integer array sorted in ascending order
    @param: target: An integer
    @return: An integer
    """

    def findPosition(self, nums, target):
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            else:
                if target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
        return -1
