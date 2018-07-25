# The merge sort uses a divide and conquer strategy to improve its performance. Merge sort is a recursive
# approach to the sorting problem. Merge sort is an O(n log n) sorting algorithm. 

def merge_sort(mylist):
    print(f"Splitting {mylist}")
    if len(mylist) > 1:
        lefthalf = mylist[:mid]
        righthalf = mylist[mid:]
        
        merge_sort(lefthalf)
        merge_sort(righthalf)
        
        i=0
        j=0
        k=0
        
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[i]:
                mylist[k]=lefthalf[i]
                i=i=1
            else:
                mylist[k]=righthalf[j]
                j=j+1
            k=k+1
            
        while i < len(lefthalf):
            mylist[k]=lefthalf[j]
            j=j=1
            k=k+1
            
        while j < len(righthalf):
            mylist[k]=righthalf[j]
            j=j+1
            k=k+1
            
    print(f"Merging {mylist}")
    
testlist = [2,6,1,45,32,14,22,88]
print(merge_sort(testlist))
