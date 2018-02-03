from pythonds.basic.queue import Queue


def hotPotato(namelist, num):
    simqueue = Queue()
    for name in namelist:
        simqueue.enqueue(name)

    while simqueue.size() > 1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())

        simqueue.dequeue()

    return simqueue.dequeue()


print(hotPotato(["Bill", "David", "Susan", "Jane", "Kent", "Brad"], 7))

# 非队列
def hotPotate(n):
    a = [1, 2, 3, 4, 5, 6, 7]
    while len(a) > 1:
        for i in range(n - 1):
            a.insert(len(a), a.pop(0))
        a.pop(0)
    return a
