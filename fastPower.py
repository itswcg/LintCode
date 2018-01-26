class Solution:
    """
    @param: a: A 32bit integer
    @param: b: A 32bit integer
    @param: n: A 32bit integer
    @return: An integer
    """

    def fastPower(self, a, b, n):
        if n == 0:
            return 1 % b
        if 1 == n:
            return a % b
        x = self.fastPower(a, b, n / 2)
        if n % 2 == 1:
            return (((x * x) % b) * a) % b
        else:
            return (x * x) % b


print(Solution().fastPower(3, 5, 7))
