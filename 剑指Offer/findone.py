class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        res = []
        for i in range(len(array)):
            if array[i] in res:
                res.remove(array[i])
            else:
                res.append(array[i])
        return res
