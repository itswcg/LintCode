class Solution:
    """
    @param: n: n pairs
    @return: All combinations of well-formed parentheses
    """

    def generateParenthesis(self, n):
        res = []
        path = ""
        self.generate(n, n, path, res)
        return res

    def generate(self, left, right, path, res):
        if left == right == 0:
            res.append(path)
        if left > 0:
            self.generate(left - 1, right, path + '(', res)
        if right > left:
            self.generate(left, right - 1, path + ')', res)
