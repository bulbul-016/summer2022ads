import random
def selectionsort(list1):
    start = time.time()
    for i in range(len(list1)-1,0,-1):
       pos_max=0
       for j in range(1,i+1):
           if list1[j]>list1[pos_max]:
               pos_max = j
       tmp = list1[i]
       list1[i] = list1[pos_max]
       list1[pos_max] = tmp
    end = time.time()
    print(f"Runtime of the program is {end - start}")

def bubbleSort(alist):
    for j in range(len(alist)-1, 0, -1):
        for i in range(j):
            if alist[i]>alist[i+1]:
                v=alist[i] 
                alist[i]=alist[i+1] 
                alist[i+1]=v

def insertion_sort(alist):
    for i in range(1, len(alist)):
        temp = alist[i]
        j = i - 1
        while (j >= 0 and temp < alist[j]):
            alist[j + 1] = alist[j]
            j = j - 1
        alist[j + 1] = temp

def mergeSort(alist):
    #print("Splitting ",alist)
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    #print("Merging ",alist)

def quickSort(nums, l, r):
    #global count
    if l < r:
        swap = l
        for run in range (l+1,r+1):            
            if nums[l] > nums[run]:
                swap += 1
                nums[swap],nums[run]=nums[run],nums[swap]

            #run += 1
        nums[l],nums[swap]= nums[swap],nums[l]
        quickSort(nums, l, swap-1)
        quickSort(nums, swap+1, r)


def check(num,clist):
    for i in clist:
        if i==num: return 1 
    else: return 2
    
a=[]
b=[]
c=[]
d=[]
'''
for i in range(15):
    a.append(random.randint(0,30))
    b.append(random.randint(0,30))
    c.append(random.randint(0,30))
'''    
for i in  a:
    if check(i,c)==2: d.append(i)
for i in b:
    if check(i,c)==2: d.append(i)

selectionsort(a)
bubbleSort(b)
insertion_sort(c)
mergeSort(d)
quickSort(a, 0, len(a)-1)

print("list a")    
print(a)
print("list b")
print(b)
print("list c")
print(c)
print("list d")
print(d)


    