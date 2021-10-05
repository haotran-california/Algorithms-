class Stack:
    def __init__(self):
        self.list = []

    def push(self, data):
        self.list.append(data)

    def pop(self):
        return self.list.pop()

    def get_stack(self):
        print(self.list)

    def is_empty(self):
        return self.list == []

    def top(self):
        if not self.list == []: #how to use functions in other functions?
            return self.list[-1]



h1 = [3, 2, 1, 1, 1]
h2 = [4, 3, 2]
h3 = [1, 1, 4, 1]

def equalStacks(h1, h2, h3):
    return 0
    #




#solve for balanced parenthesis
# "()()" , ({{()}}), [{()}]

def balanced_paren():
    return 0


#



#implement a queue with two stacks
#first in first out
# class Queue():
#
#     def __init__(self):
#         self.list = []
#         self.stack1 = Stack()
#         self.stack2 = Stack()
#
#     def enqueue(self, data):
#         self.stack1.push(data)
#
#     def dequeue(self):
#         flag = True
#         while flag == True:
#             if self.stack1.is_empty():
#                 flag = False
#                 break
#             else:
#                 self.stack2.push(stack1.pop())
#
#         return self.stack2.pop()


class Queue():

    def __init__(self, data):
        self.list



array = [1, 2, 3, 4, 5]
queue = Queue()

for i in array:
    queue.enqueue(i)

print(queue.dequeue())

#why do you have to use self to access the properties in the class?
