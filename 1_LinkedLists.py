# Creating the linkedList with 3 nodes
# Class which containes the node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def listOut(self):
        temp = self.head
        while (temp):
            print (temp.data)
            temp = temp.next    

if __name__ == "__main__":
    # Creating the empty list
    empty_list = LinkedList()

    # Initialising the nodes
    empty_list.head = Node(1)
    second = Node(2)
    third = Node(3)

    # Linking the nodes with one another
    empty_list.head.next = second
    # Checking the output by not linking the initialised node.
    # second.next = third

    empty_list.listOut()
    print (empty_list.head.data, second.data, third.data)