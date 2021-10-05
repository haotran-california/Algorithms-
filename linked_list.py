#linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def _print(self):
        if self.head == None:
            print("no values stored in linked list")
        else:
            n = self.head
            while n != None:
                print(n.data)
                n = n.next

    def add(self, data):
        new_node = Node(data)
        n = self.head
        if self.head == None:
            self.head = new_node
        else:
            self.head = new_node
            self.head.next = n #how is it possible to use a method of the class Node in a separate class linked listed?
                                #is it because self.head points to a node which then you can call the method next?

    def add_begining(self, data): #how is the value of the last node still able to be Null
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def add_end(self, data): #why does this operation seem to take so long?
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            n = self.head
            while n.next != None: #when can I use n versus n.next when in my while loop
                n = n.next
            n.next = new_node

    def insert(self, data, insert):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            n = self.head
            while n is not None:
                if n.data == insert:
                    break
                else:
                    n = n.next
            new_node.next = n.next
            n.next = new_node

    def insert_before(self, data, x):
        new_node = Node(data)
        #check if x is the value of the first node
        if self.head == None:  #should I define n = this.head here or use this.head
            new_node.next = self.head
            self.head = new_node

        if x == self.head.data:
            new_node.next = self.head
            self.head = new_node
        else:
            n = self.head #since we don't want to alter the self.head we use a variable leaving this value the same
            while n.next != None:
                if n.next.data == x:
                    break
                else:
                    n = n.next
            new_node.next = n.next
            n.next = new_node

    def delete_begining(self):

        if self.head == None:
            return print("This linked list is empty and cannot be deleted")
            #either use a if else structure or return
        self.head = self.head.next



    def delete_end(self):
        if self.head == None:
            print("This linked list is empty and cannot be deleted")
        elif self.head.next == None:
            self.head = None
        else:
            n = self.head
            while n.next.next != None:
                n = n.next
            n.next = None

    def delete_by_value(self, value):
        if self.head is None:
            print("Linked list is empty")
            return
        if self.head.data == value:
            self.head = self.head.next
            return

        else:
            n = self.head
            while n.next != None:
                if n.next.data == value:
                    break
                else:
                    n = n.next
            if n.next == None:
                print('Node is not found')
            n.next = n.next.next

    def deleteDups(self):
        current = self.head
        while current is not None:
            runner = current
            while runner.next is not None:
                if runner.next.data == current.data:
                    runner.next = runner.next.next
                else:
                    runner = runner.next
            current = current.next

    def reverseLL(self):

        if self.head is None:
            return print("this is an empty linked list")

        last = None
        current = self.head
        next = self.head.next

        while current.next is not None:
            #reverse the direction of pointers
            current.next = last
            #increment each pointer
            last = current
            current = next
            next = next.next

        #tail of list becomes the head
        current.next = last
        self.head = current

    def detectCycle(self):
        #use two pointers one fast and one slow to go through the linked listed
        #if the two pointers land on eachother than there is a cycle
        #this can also be done with a hashmap or by marking the nodes as visited
        return 0










ll = LinkedList()
for i in range(4):
    ll.add_end(i)
ll._print()

def getNode(head, p):

    l = 0
    while head.next != None:
        l += 1
        head = head.next
    print(l)

getNode(ll.head, 4)












#something = new_node
#inserts the node after
#new_node = n.next inserts the node before
#then how do you transverse and move all the nodes to the right?
