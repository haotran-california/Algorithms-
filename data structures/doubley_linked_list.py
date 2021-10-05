class Node:
    def __init__(self, data):
        self.next = None
        self.previous = None
        self.data = data

class LinkedList:
    def __init__(self):
        self.head = None

    def add_begining(self, data):

        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node

    def add_end(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            n = self.head
            while n.next is not None:
                n = n.next
            n.next = new_node
            new_node.previous = n

    #fix this
    def insertion_before(self, insert, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            n = self.head
            while n.next.data == insert:
                n = n.next

            new_node.previoius = n
            new_node.next = n.next.next
            n.next.next.previous = n
            n.next = new_node

    def delete_begining(self):
        if self.head == None:
            print("empty")
        else:
            n = self.head
            self.head = n.next
            n.next.previous = None
            n.next = None

    def delete_end(self):
        if self.head == None:
            print("empty")
        else:
            n = self.head
            while n.next.next is not None:
                n = n.next

            n.next.previous = None
            n.next = None


    def printLinkedList(self):
        if self.head == None:
            print("empty")
        else:
            n = self.head
            while n is not None:
                print(n.data, " -> ", end="")
                n = n.next


LL = LinkedList()
LL.add_begining(10)
LL.add_begining(5)
LL.add_begining(1)
LL.add_end(20)

LL.printLinkedList()
