class Solution:
    """
    @param: A: A string
    @param: B: A string
    @return: if string A contains all of the characters in B return true else return false
    """

    def compareStrings(self, A, B):
        i = 0
        a = list(A)
        b = list(B)
        r = 0
        while i < len(a):
            j = 0
            while j < len(b):
                if b[j] == a[i]:
                    a.remove(a[i])
                    b.remove(b[j])
                    r += 1
                else:
                    j += 1
            else:
                i += 1
        if r == len(B):
            return True
        else:
            return False


print(Solution().compareStrings('ABCD', 'AABC'))
