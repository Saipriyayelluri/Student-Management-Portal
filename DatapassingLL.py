from DetailsRegister import regis


class Node:
    # Function to initialise the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null


# Linked List class contains a Node object
class LinkedList:
    # Function to initialize head
    def __init__(self):
        self.head = None


# Code execution starts here
if __name__ == '__main__':
    # Start with the empty list
    llist = LinkedList()
    llist.head = Node(regis())
