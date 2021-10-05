class _Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def add_node(self, current, data):
        #check if the data is greater than or less than the current node
        if data <= current.data:
            if current.left == None:
                child = _Node(data)
                current.left = child
            else:
                self.add_node(current.left, data)  #why use self in front of your function?, why no return statement to use recursion here?
        else:
            if current.right == None:
                child = _Node(data)
                current.right = child
            else:
                self.add_node(current.right, data)

    def PostOrder(self, root):
        if root:
            self.PostOrder(root.left)
            self.PostOrder(root.right)
            print(root.data)

    def getHeight(self, root):
        if root:
            left_height = self.getHeight(root.left)
            right_height = self.getHeight(root.right)

            if (right_height > left_height):
                return right_height + 1
            else:
                return left_height + 1
        else:
            return 0




list = []
root = _Node(10)
root.add_node(root, 5)
root.add_node(root, 12)
root.add_node(root, 3)
root.add_node(root, 18)
print(root.getHeight(root))
