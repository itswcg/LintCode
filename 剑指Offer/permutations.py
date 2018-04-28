class Solution:
    def Permutation(self, ss):
        from itertools import permutations
        if not ss: return []
        return sorted(list(set(map(''.join, permutations(ss)))))
