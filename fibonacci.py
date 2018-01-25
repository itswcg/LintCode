class Solution:
    """
    @param: n: an integer
    @return: an ineger f(n)
    """

    def fibonacci(self, n):
        a = [0, 1]
        for i in range(2, n):
            a.append(a[i - 2] + a[i - 1])
        return a[n - 1]


print(Solution().fibonacci(10))
