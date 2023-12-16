class Node:
    def __init__(self, data):
        self.data = data
        self.pointer = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        """
        Adds a node to the end of a linked list
        Makes node the head of list, if the list is empty at first
        """

        node = Node(data)

        if self.head is None:
            self.head = node
        else:
            currentNode = self.head
            while True:
                if currentNode.pointer is None:
                    currentNode.pointer = node
                    break
                currentNode = currentNode.pointer
    
    def prepend(self,data):
        """
        Add a node to the first element of the list
        """
        new_node = Node(data)
        tempNode = self.head
        new_node.pointer = tempNode
        self.head = new_node
        del tempNode
    
    def insert(self, data, index):
        """
        Insert a node at any given index
        """
        if index == 0:
            self.prepend(data)
            return

        if index == self.length():
            self.append(data)
            return
        
        if index <= 0 or index > self.length():
            print('Not a valid index')
            return
        
        node = Node(data)
        currentNode = self.head
        currentIndex = 0

        while True:
            if currentIndex == index:
                prevNode.pointer = node
                node.pointer = currentNode
                break
            currentIndex += 1
            prevNode = currentNode
            currentNode = prevNode.pointer

    def pop(self):
        currentNode = self.head
        while True:
            if currentNode.pointer is None:
                prevNode.pointer = None
                break
            prevNode = currentNode
            currentNode = prevNode.pointer

    def length(self):
        """
        Get's the length of the list and returns it
        """
        length = 0
        currentNode = self.head
        while True:
            if currentNode is None:
                break
            length += 1
            currentNode = currentNode.pointer
        
        print(length)
        return length
    
    def display(self):
        """
        Displays the linked list in the form as an array
        """
        vals = []
        currentNode = self.head
        while True:
            if currentNode is None:
                break
            vals.append(currentNode.data)
            currentNode = currentNode.pointer
        print(vals)
        return vals
        
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.prepend(0)
ll.append(4)
ll.display()
ll.insert(3,3)
ll.display()
ll.pop()
ll.display()