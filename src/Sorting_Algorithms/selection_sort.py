# The Selection Sort is an upgrade from Bubble Sort. This sorting algorithm sorts
# structures in O(n^2) which is not an improvement in time complexity, however, there is
# a reduction in exchanges.

def selectSort(mylist):
    for fillingslot in range(len(mylist)-1,0,-1):
        posofMax=0
        for loc in range(1,fillingslot+1):
            if mylist[loc]>mylist[posofMax]:
                posofMax=loc
                
        temp=mylist[fillingslot]
        mylist[fillingslot]=mylist[posofMax]
        mylist[posofMax]=temp
        
testlist = [56,76,24,22,2,7,65,98]
selectionSort(mylist)
print(mylist)
