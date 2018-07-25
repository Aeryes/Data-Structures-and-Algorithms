# The shell sort improves on the insertion sort by breaking the original list into a
# number of smaller sublists, each of which is sorted using an insertion sort. A shell
# sort performs somewhere in the range between O(n) and O(n^2).

def shell_sort(mylist):
    sublistcounter = len(mylist)//2
    while sublistcounter > 0:
        
        for startpos in range(sublistcounter):
            gap_insertion_sort(mylist, startpos, sublistcounter)
            
            print(f"After increments of size {sublistcounter}, The list is {mylist}")
            
            sublistcounter = sublistcounter//2
            
def gap_insertion_sort(mylist, start, gap):
    for i in range(start + gap, len(mylist), gap):
        
        currentval=mylist[i]
        pos=i
        
        while pos >= gap and mylist[pos - gap] > currentval:
            mylist[pos]=mylist[pos - gap]
            pos=pos - gap
            
        mylist[pos]=currentval
        
testlist = [54,76,23,4,56,89,12]
print(shell_sort(testlist))
