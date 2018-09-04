# Insertion Sort is similar to Bubble Sort and Selection Sort in regards to time complexity, 
# however it approaches the problem in a different way. It always maintains a sorted sublist in the 
# of the list. Each new item is then 'inserted' into the previous sublist so that
# the sorted sublist is one item larger.

def insertSort(mylist):
    for index in range(1,len(mylist)):
        currentval=mylist[index]
        pos=index
        
        while pos>0 and mylist[pos-1]>currentval:
            mylist[pos]=mylist[pos-1]
            pos=pos-1
            
        mylist[pos]=currentval
        
testlist = [43,65,87,2,34,55,98,1]
insertSort(testlist)
print(testlist)
