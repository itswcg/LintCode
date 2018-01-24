class Solution:
    """
    @param: nums: A list of integers.
    @return: A list of permutations.
    """

    def permute(self, nums):
        from itertools import permutations
        return list(permutations(nums))


print(Solution().permute([1, 2, 3]))
