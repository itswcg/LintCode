# 1,1,2,3...
class Solution:
    def Fibonacci(self, n):
        l = [0, 1]
        for i in range(2, n+1):
            l.append(l[i-1]+l[i-2])
        return l[n]

    def fib1(self, n):
        a, b = 0, 1
        for i in range(n):
            a, b = b, a+b
        return a

    def fib2(self, n):
        if n < 2:
            return n
        else:
            return self.fib2(n-1) + self.fib2(n-2)
