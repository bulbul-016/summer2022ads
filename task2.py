def binary_search_iterative(array, element):
    mid = 0
    start = 0
    end = len(array)-1
    step = 0 #this value is for counting iterations

    while (start <= end):
        step = step+1
        mid = (start + end) // 2
        if element == array[mid]: #if we find number we will return like this
            return 'number of iterations is equal to '+ str(step)
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
print(binary_search_iterative(a,x))
