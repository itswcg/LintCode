class Solution:
    """
    @param arr:  an array of non-negative integers
    @return: minimum number of elements
    """

    def minElements(self, arr):
        arr.sort()
        for i in range(len(arr) - 1, -1, -1):
            if sum(arr[i:]) > sum(arr[:i]):
                return len(arr[i:])
