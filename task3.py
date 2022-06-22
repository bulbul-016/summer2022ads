def bubbleSort(alist): #we will sort our array
    for j in range(len(alist)-1, 0, -1):
        for i in range(j):
            if alist[i]>alist[i+1]:
                v=alist[i] 
                alist[i]=alist[i+1] 
                alist[i+1]=v


def binary_search_iterative(array, element):
    mid = 0
    start = 0
    end = len(array)-1
    step = 0 #this value is for counting iterations

    while (start <= end):
        step = step+1
        mid = (start + end) // 2
        if element == array[mid]: #if we find number we will return like this
            return 'We find our number for '+ str(step) + ' iterations and my names lenght is equal to ' + str(array[mid])
        if element < array[mid]:
            # We will continue the search in the left half
            end = mid - 1
        else:
            # Continue the search in the right half
            start = mid + 1
    #if we can not find number which we look for
    return 'Element is not present in array' #if we can not find number which we look for

#first of all we will get input 
a=list(map(int, input().split(',')))
#then we will get our number which we want to search
x=int(input())
#if array is not sorted we will sort it 
bubbleSort(a)
print(binary_search_iterative(a,x))

'''
1,2,3,4,5,6,7,8,9,10,11,12
6
We find our number for 1 iterations and my names lenght is equal to 6
'''