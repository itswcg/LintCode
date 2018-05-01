class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        if pRoot is None:return []
        stack = [pRoot]
        res = []
        while stack:
            tmp = []
            for i in range(len(stack)):
                p = stack.pop(0)
                if p.left:
                    stack.append(p.left)
                if p.right:
                    stack.append(p.right)
                tmp.append(p.val)
            res.append(tmp)
        return res
