class Solution:
    """
    @param x: the wall's height
    @return: YES or NO
    """

    def isBuild(self, x):
        if x in [3, 7]:
            return YES
        else:
            for i in [3, 7]:
                x -= i
                if x in [3, 7]:
                    return YES
                else:
