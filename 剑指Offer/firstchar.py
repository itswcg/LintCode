class Solution:
    def FirstNotRepeatingChar(self, s):
        res = []
        for i in s:
            if s.count(i) == 1:
                res.append(i)
                break
        if len(res) == 0: return -1
        return s.index(res[0])
