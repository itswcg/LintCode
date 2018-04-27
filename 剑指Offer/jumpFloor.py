class Solution:
    def jumpFloor(self, number):
        rec = [1, 1]
        for i in range(2, number+1):
            rec.append(rec[i-1]+rec[i-2])
        return rec[number]
