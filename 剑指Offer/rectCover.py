class Solution:
    def rectCover(self, number):
        if number == 0:
            return 0
        else:
            rec = [1, 1]
            for i in range(2, number+1):
                rec.append(rec[i-1]+rec[i-2])
            return rec[number]