def bubbleSort(arr):
    n = len(arr)
    swapped = False
    
    for i in range(n-1):
        for j in range(n//2, n-i-1):
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                # print(arr)
        
        for l in range(0, n//2):
            if arr[l] < arr[l + 1]:
                swapped = True
                arr[l], arr[l + 1] = arr[l + 1], arr[l]
                # print("*",arr)

        if not swapped:
            return

alist=[input().split()]
bubbleSort(alist)