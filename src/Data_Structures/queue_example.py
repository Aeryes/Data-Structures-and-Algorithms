# Example of a Queue in Python. Queues are very useful data structures that are
# seen in many different locations in the tech industry and outside of the tech
# industry. If many people are using a printer, their jobs are placed in a queue and
# executed one at a time.

# The pop() function runs in 0(n) time or linear time. The rest of the functions run in O(n) time or constant time. 
class Queue():
    def __init__(self):
        self.items = []
    
    def __len__(self):
        return len(self.items)
    
    def is_empty(self):
        print(self.items == [])
        
    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if not self.items:
            print("The Queue is empty.")
        else:
            self.removed = self.items.pop()
            print(f"{self.removed} + has been removed from the Queue.")

# To use the queue simply create a Queue instance and use the method calls as seen in 
# the example below.
myqueue = Queue()
print(len(myqueue))
myqueue.enqueue('sfsf')
myqueue.dequeue()
myqueue.is_empty()
