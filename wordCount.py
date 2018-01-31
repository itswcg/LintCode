class WordCount:

    # @param {str} line a text, for example "Bye Bye see you next"
    def mapper(self, _, line):
        words = line.split()
        for word in words:
            yield word, 1

    # @param key is from mapper
    # @param values is a set of value with the same key
    def reducer(self, key, values):
        yield key, len(values)
