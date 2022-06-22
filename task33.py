def bubbleSort(alist): 
    for j in range(len(alist)-1, 0, -1): 
        for i in range(j): 
            if alist[i]>alist[i+1]: 
                v=alist[i]  
                alist[i]=alist[i+1]  
                alist[i+1]=v 
 
 
def binary_search_iterative(array, element): 
    mid = 0 
    start = 0 
    end = len(array) 
    step = 0 
 
    while (start <= end):
        step = step+1 
        mid = (start + end) // 2 
        print('step ',step) 
        print(array[start:end+1])
        if element == array[mid]: 
            return 'We find our number for '+ str(step) + ' iterations and my names lenght is equal to ' + str(array[mid]) 
        if element < array[mid]: 
            end = mid - 1 
        else: 
            start = mid + 1 
    return 'Element is not present in array' 
 
a=list(map(int, input().split(','))) 
x=int(input()) 
#bubbleSort(a) 
print(binary_search_iterative(a,x))