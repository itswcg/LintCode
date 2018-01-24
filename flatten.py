class Solution(object):

    # @param nestedList a list, each element in the list
    # can be a list or integer, for example [1,2,[1,2]]
    # @return {int[]} a list of integer
    def flatten(self, nestedList):
        if isinstance(nestedList, int):
            return [nestedList]
        result = []
        for i in nestedList:
            result.extend(self.flatten(i))
        return result


print(Solution().flatten([4, [3, [2, [1]]]]))
