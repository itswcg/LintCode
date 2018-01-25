class Solution:
    """
    @param: dictionary: an array of strings
    @return: an arraylist of strings
    """

    def longestWords(self, dictionary):
        l = []
        max = 0
        for word in dictionary:
            n = len(word)
            if n > max:
                max = n
                l = []
                l.append(word)
            elif n == max:
                l.append(word)
        return l


print(Solution().longestWords({
    "like",
    "love",
    "hate",
    "yes"
}))
