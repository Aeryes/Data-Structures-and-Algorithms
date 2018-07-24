# Example of a DeQueue in Python. A DeQueue is a versatile data structure which
# acts as a queue from two ends. This gives the programmer more control over how
# to set up and add or remove from the dequeue.
class DeQueue():
    def __init__(self):
        self.items = []
        
    def __len__(self):
        if not self.items:
            print("The dequeue is empty.")
        else:
            return len(self.items))
        
    def is_empty(self):
        print(self.items == [])
        
    def add_rear(self, item):
        self.items.append(item)
        print(f"{item} + added to the rear.")
        
    def add_front(self, item):
        self.items.insert(0, item)
        print(f"{item} + has een added to the front.")

    def remove_rear(self):
        if self.items == []:
            print("The dequeue is empty.")
        else:
            print(f"{self.items.pop()} + has been removed from the rear.")
        
    def remove_front(self):
        if self.items == []:
            print("The dequeue is empty.")
        else:
            print(f"(self.items.pop(0)} + has been removed from the front.")

# In order to use this data structure simply create a class instance and use the method calls
# like seen in the sample code below.
mydequeue = DeQueue()
mydequeue.add_rear(6)
mydequeue.add_front(2)
mydequeue.is_empty()
mydequeue.remove_rear()
len(mydequeue)
mydequeue.remove_front()
mydequeue.remove_rear()
