class Solution:
    def LastRemaining_Solution(self, n, m):
        if n == 0 or m == 0: return -1
        res = [i for i in range(n)]
        while len(res) != 1:
            for i in range(m-1):
                res.insert(len(res)-1, res.pop(0))
            res.pop(0)
        return res[0]
