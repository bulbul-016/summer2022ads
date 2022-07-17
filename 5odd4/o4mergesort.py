import time
start = time.time()

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


def check(num,clist):
    for i in clist:
        if i==num: return 1 
    return 2
    
a=[15, 9, 10, 8, 7, 16, 4, 20, 18, 9, 12, 3, 14, 15, 13, 101]
b=[13, 8, 20, 1, 15, 6, 10, 2, 6, 9, 8, 12, 18, 16, 5, 101]
c=[7, 18, 1, 10, 6, 3, 19, 7, 12, 20, 3, 6, 11, 7, 3, 101]
d=[]
for i in  a:
    if check(i,b)==1:
        if check(i,c)==1: d.append(i)  

mergeSort(a)
mergeSort(b)
mergeSort(c)
mergeSort(d)

print("list a")    
print(a)
print("list b")
print(b)
print("list c")
print(c)
print("list d")
print(d)

end = time.time()
print(f"Runtime of the program is {end - start}")