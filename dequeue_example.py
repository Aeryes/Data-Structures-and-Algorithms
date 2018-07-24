# Example of a DeQueue in Python. A DeQueue is a versatile data structure which
# acts as a queue from two ends. This gives the programmer more control over how
# to set up and add or remove from the dequeue.
class DeQueue():
    def __init__(self):
        self.items = []
        
    def __len__(self):
        if self.items == []:
            print("The dequeue is empty.")
        else:
            return len(self.items))
        
    def isEmpty(self):
        print(self.items == [])
        
    def addRear(self, item):
        self.items.append(item)
        print(str(item) + " has been added to the rear.")
        
    def addFront(self, item):
        self.items.insert(0, item)
        print(str(item) + " has een added to the front.")

    def removeRear(self):
        if self.items == []:
            print("The dequeue is empty.")
        else:
            print(str(self.items.pop()) + " has been removed from the rear.")
        
    def removeFront(self):
        if self.items == []:
            print("The dequeue is empty.")
        else:
            print(str(self.items.pop(0)) + " has been removed from the front.")

# In order to use this data structure simply create a class instance and use the method calls
# like seen in the sample code below.
mydequeue = DeQueue()
mydequeue.addRear(6)
mydequeue.addFront(2)
mydequeue.isEmpty()
mydequeue.removeRear()
mydequeue.size()
mydequeue.removeFront()
mydequeue.removeRear()
