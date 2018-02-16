class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @param target: An integer
    @return: return the sum of the three integers, the sum closest target.
    """

    def threeSumClosest(self, numbers, target):
        numbers.sort()
        res = None
        for i in range(len(numbers)):
            l, r = i + 1, len(numbers) - 1
            while l < r:
                sum = numbers[i] + numbers[r] + numbers[l]
                if res is None or abs(sum - target) < abs(res - target):
                    res = sum
                if sum <= target:
                    l += 1
                else:
                    r -= 1
        return res
