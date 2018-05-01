class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        for i in range(len(numbers)):
            if numbers.count(numbers[i]) > 1:
                duplication[0] = numbers[i]
                return True
                break
        return False
