# This is an example of sequential search hard-coded in Python. This searching
# algorithm is already natively implemented into Python through the use of
# the 'in' keyword. The time complexity of the search is O(n).

def seqSearch(mylist, item):
    position=0
    found_item=False
    
    while position<len(mylist) and not found_item:
        if mylist[position]==item:
            found_item=True
        else:
            position=position+1
            
    return found_item
    
testlist = [1,2,32,6,3,76,23,43]
print(seqSearch(testlist, 32))
