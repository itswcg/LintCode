class Solution:
    """
    @param s: a string represent DNA sequences
    @return: all the 10-letter-long sequences
    """

    def findRepeatedDna(self, s):
        res = []
        for i in range(0, len(s) - 9):
            tmp = s[i: i + 10]
            res.append(tmp)
        a = set(res)
        s = []
        for item in a:
            if res.count(item) > 1:
                s.append(item)
        return s


print(Solution().findRepeatedDna("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))
