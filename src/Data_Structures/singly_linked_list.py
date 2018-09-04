# Here is an example of a Singly Linked List in Python.

class Node():
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

class LinkedList():
    def __init__(self, head=None):
        self.head = head

    def insert(self, data):
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node
        print(f'{data} has been added to the linked list.')

    def __len__(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next_node
        print(count)

    def search(self, data):
        current = self.head
        found = False
        while current and found is False:
            if current.data == data:
                found = True
                print(f'{data} has been found!')
            else:
                current = current.next_node
        if current is None:
            print(f'{data} not found!')

    def delete(self, data):
        current = self.head
        previous = None
        found = False
        while current and found is False:
            if current.data == data:
                found = True
            else:
                previous = current
                current = current.next_node
        if current is None:
            print(f'{data} not found!')
        if previous is None:
            self.head = current.next_node
        else:
            previous.next_node = current.next_node
        print(f'{data} has been removed from the linked list.')

mylinkedlist = LinkedList()
mylinkedlist.insert(50)
mylinkedlist.insert(20)
mylinkedlist.__len__()
mylinkedlist.search(50) 
mylinkedlist.search(45)
mylinkedlist.delete(50)
mylinkedlist.__len__()