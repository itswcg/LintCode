class Solution:
    def GetUglyNumber_Solution(self, index):
        if index <= 0: return 0
        if index == 0: return 1
        res = [1]
        t2, t3, t5 = 0, 0, 0
        for i in range(1, index):
            res.append(min(2*res[t2], 3*res[t3], 5*res[t5]))
            if res[i] == res[t2]*2:
                t2 += 1
            if res[i] == res[t3]*3:
                t3 += 1
            if res[i] == res[t5]*5:
                t5 +=1
        return res[index-1]
