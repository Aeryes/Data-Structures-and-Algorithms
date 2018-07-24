# The following code shows a working example of Bubble Sort in Python. This sorting algorithm
# is not very effective due to its bad time complexity of O(n^2). This algorithm is still important
# to learn as it is a stepping stone to move onto more complex searching algorithms.

def bubbleSort(mylist):
    for passingnum in range(len(mylist)-1,0,-1):
        for i in range(passingnum):
            if mylist[i]>mylist[i+1]:
                tempnum=mylist[i]
                mylist[i]=mylist[i+1]
                mylist[i+1]=temp
                
testlist = [54,67,23,1,3,7,76,45]
bubbleSort(mylist)
print(mylist)
