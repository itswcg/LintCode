class MyQueue:

    def __init__(self):
        self.item = []

    """
    @param: element: An integer
    @return: nothing
    """

    def push(self, element):
        self.item.insert(0, element)

    """
    @return: An integer
    """

    def pop(self):
        return self.item.pop()

    """
    @return: An integer
    """

    def top(self):
        return self.item[-1]
