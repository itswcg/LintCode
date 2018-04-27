class Solution:
    def jumpFloorII(self, number):
        rec = [1, 1]
        for i in range(2,number+1):
            rec.append(2*rec[i-1])
        return rec[number]
