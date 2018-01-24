class Solution:
    """
    @param: numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
    """

    def threeSum(self, numbers):
        numbers.sort()
        n = list(numbers)
        s = []
        for i in range(len(numbers) - 2):
            for j in range(i + 1, len(numbers) - 1):
                for k in range(j + 1, len(numbers)):
                    if n[i] + n[j] + n[k] == 0:
                        if [n[i], n[j], n[k]] not in s:
                            s.append([n[i], n[j], n[k]])
        return list(s)


print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))
