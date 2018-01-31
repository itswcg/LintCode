class Solution:
    """
    @param: : the 1st string
    @param: : the 2nd string
    @return: uncommon characters of given strings
    """

    def concatenetedString(self, s1, s2):
        ss1 = list(s1)
        ss2 = list(s2)
        s = []
        for i in range(len(ss1)):
            if ss1[i] not in ss2:
                s.append(ss1[i])
        for j in range(len(ss2)):
            if ss2[j] not in ss1:
                s.append(ss2[j])
        return ''.join(s)


print(Solution().concatenetedString('aacdb', 'gafd'))
