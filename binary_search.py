# This is an example of a binary search algorithm in Python using a recursive/divide and conquer approach.
# In a binary search algorithm we start with a midpoint of a sorted list. Once we have this midpoint we then
# use it to find out if the item we want to find is in the lower or upper half of the list.
# This is done in O(n/2  +n/4+...) = O(n) time. It is important to remember that binary search is done on a sorted list or structure.

# Implementation one, recursive approach.
def binarysearch(mylist, item):
    if len(mylist)==0:
        return False
    else:
        midpoint=len(mylist)//2
        if myslist[midpoint]==item:
            return True
        else:
            if item<mylist[midpoint]:
                return binarySearch(mylist[:midpoint], item)
            else:
                return binarySearch(mylist[midpoint+1:], item)
                
testlist = [1,2,3,4,5,6,7,8,9,10]
print(binarysearch(testlist, 3)

# Implementation two, iterative appraoch.
def binary_search(array, target):
    lower_number=0
    upper_number=len(array)
    while lower_number < upper_number:  
        x=lower_number + (upper_number - lower_number)//2
        val=array[x]
        if target==val:
            return x
        elif target > val:
            if lower_number==x:   
                break        
            lower_number=x
        elif target < val:
            upper_number=x
      
print(binary_search([20,3,12,5,6,7,11],5))
