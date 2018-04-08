#Merge Sort#


def merge(left, right):
    if len(left) == 0 and len(right) == 0:
        return "Error"
    i = 0
    j=0
    k = 0 
    mergedL = []
    sortedL=[]


    while len(mergedL) < (len(left) + len(right)):
        if i == len(left) :
            mergedL += right[j:]
            break
        if j == len(right) :
            mergedL += left[i:]
            break
        if left[i] >= right[j]:
            mergedL += [right[j]]
            j += 1
        else:
            mergedL += [left[i]]
            i +=1
    if len(sortedL) == 0:
        sortedL += mergedL
        mergedL[:] = []

    return sortedL
    
    

            

def mergeSort(l):
    left = []
    right =[]

    if len(l) <= 1:
        return l
    else:
        left = mergeSort(l[:(len(l)/2)])
        right = mergeSort(l[len(l)/2:])
    return merge(left,right)
    




