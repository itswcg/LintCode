class Solution:
    def ReverseSentence(self, s):
        ss = s.split(' ')
        return ' '.join(ss[::-1])

s = 'student. a am I'
print(s.split(' '))
