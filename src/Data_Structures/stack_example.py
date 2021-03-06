# Example of a Stack in Python. Stacks are useful data structures
# that are used in a variety of circumstances in the real world such
# as the back and forward buttons on search pages. Stacks are O(1) meaning
# they are in constant time.

class Stack():
    def __init__(self):
        self.items = []
        
    def __len__(self):
        return len(self.items)
    
    def is_empty(self):
        print(self.items == [])
        
    def push(self, item):
        self.items.append(item)
        print("Item " + f"{item} +  added to the Stack")
        
    def peek(self):
        if not self.items:
            print("Empty Stack")
        else:
            print(self.items[-1])
        
    def pop(self):
        if self.items == []:
            print("Cannot remove items from empty list.")
        else:
            return self.items.pop()

# To create a stack simply make an instance of the class and use
# the method calls as required. An example is shown below.

mystack = Stack()
mystack.peek()
print(len(mystack))
mystack.is_empty()
mystack.pop()
mystack.push(15)
