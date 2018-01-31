"""
The guess API is already defined for you.
@param num, your guess
@return -1 if my number is lower, 1 if my number is higher, otherwise return 0
you can call Guess.guess(num)
"""


class Solution:
    # @param {int} n an integer
    # @return {int} the number you guess
    def guessNumber(self, n):
        start, end = 1, n
        while True:
            mid = (start + end) // 2
            res = Guess.guess(int(mid))
            if res == 0:
                return mid
            else:
                if res == -1:
                    end = mid - 1
                else:
                    start = mid + 1
