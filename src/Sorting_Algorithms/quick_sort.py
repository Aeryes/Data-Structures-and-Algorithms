# The quick sort uses divide and conquer to gain the advantages that merge sort has, 
# while not using additional storage. Sometimes it is possible that the 
# list may not be divided in half which can lead to a performance decrease.

def quick_sort(mylist):
    quick_sort_helper(mylist, 0, len(mylist)-1)
    
def quick_sort_helper(mylist, first, last):
    if first < last:
        splitpoint = partition(mylist, first, last)
        
        quick_sort_helper(mylist, first, splitpoint-1)
        quick_sort_helper(mylist, splitpoint+1, last)
        
def partition(mylist, first, last):
    pivot_val=mylist[first]
    
    left_mark=first+1
    right_mark=last
    
    done=False
    while not done:
        while left_mark <= right_mark and mylist[left_mark] <= pivot_val:
            left_mark=left_mark+1
            
        while mylist[right_mark] >= pivot_val and right_mark >= left_mark:
            right_mark=right_mark-1
            
        if right_mark < left_mark:
            done=True
        else:
            temp_val=mylist[first]
            mylist[left_mark]=mylist[right_mark]
            mylist[right_mark]=temp_val
            
    temp_val=mylist[first]
    mylist[first]=mylist[right_mark]
    mylist[right_mark]=temp_val
    
    return right_mark
    
testlist = [2,54,3,77,14,34,7]
print(quick_sort(testlist))
