# Hashing is a very time effective way to search and store information in a structure.
# This method uses hash tables to store and quickly find required information. A hash
#function assigns values to their respective slots It performs in O(1) time. 

class HashTable():
    def __init__(self):
        self.size=11
        self.slots=[None]*self.size
        self.data=[None]*self.size
        
    def put(self, key, data):
        hashval=self.hashfunction(key, len(self.slots))
        
        if self.slots[hashval]==None:
            self.slots[hashval]=key
            self.data[hashval]=data
        else:
            if self.slots[hashval]==key:
                self.data[hashval]=data
            else:
                next_slot=self.rehash(hashval, len(self.slots))
                while self.slots[next_slot] != None and self.slots[next_slot] != key:
                    next_slot-self.rehash(next_slot, len(self.slots))
                    
                if self.slots[next_slot]==None:
                    self.slots[next_slot]=key
                    self.data[next_slot]=data
                else:
                    self.data[next_slot]=data
                    
    def hashfunction(self, key, size):
        return key%size
        
    def rehash(self, old_hash, size):
        return (old_hash)%size
        
    def get(self, key):
        starting_slot=self.hashfunction(key, len(self.slots))
        
        data=None
        stop=False
        found=False
        pos=starting_slot
        
        while self.slots[pos] != None and not found and not stop:
            if self.slots[pos]==key:
                found==True
                data=self.data[pos]
            else:
                pos=self.rehash(pos, len(self.slots))
                if self.pos==starting_slot:
                    stop=True
        return data
        
    def __getitem__(self, key):
        return self.get(key)
        
    def __setitem__(self, key):
        return self.put(key, data)
        
H = HashTable()
H[54]="cat"
H[26]="dog"
H[93]="lion"
H.slots
H.data
print(H[99])
