def bubbleSort(alist):
    for j in range(len(alist)-1, 0, -1):
        for i in range(j):
            if alist[i]>alist[i+1]:
                v=alist[i] 
                print(v)
                alist[i]=alist[i+1] 
                print(alist[i])
                alist[i+1]=v

alist=[input().split()]
bubbleSort(alist)
print(alist)