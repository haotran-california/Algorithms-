class Queue:
    def __init__(self):
        self.list = []

    def enqueue(self, data):
        self.list.append(data)

    def dequeue(self):
        return self.list.pop(0)

    def front(self):
        return self.list[0]

    def rear(self):
        return self.list[-1]

    def get_queue(self):
        print(self.list)

q = Queue()
q.enqueue('A')
q.enqueue('B')
q.enqueue('C')
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())




class Solution:
    def __init__(self):
        self.stack = []
        self.queue = []

    def pushCharacter(self, data):
        self.stack.append(data)

    def enqueueCharacter(self, data):
        self.queue.append(data)

    def popCharacter(self):
        return self.stack.pop()

    def dequeueCharacter(self):
        return self.queue.pop(0)

def palidrome(input):
    s = Solution()

    #add the whole string into the stack and queue
    for i in input:
        s.pushCharacter(i)
        s.enqueueCharacter(i)
    #if both the stack and queue are cleared then the condition in the while loop returns
    while s.popCharacter() == s.dequeueCharacter():
        if s.stack == [] and s.queue == []:
            return print(input, " is a palidrome")

    #if both stack and queue are not completely cleared than this is returned instead
    return print(input, "is not a palidrome")


string = '10101010'
