import time
start = time.time()

def bubbleSort(alist):
    for j in range(len(alist)-1, 0, -1):
        for i in range(j):
            if alist[i]>alist[i+1]:
                v=alist[i] 
                print(v)
                alist[i]=alist[i+1]
                print(alist[i]) 
                alist[i+1]=v

def check(num,clist):
    for i in clist:
        if i==num: return 1 
    else: return 2
    
a=[15, 9, 10, 8, 7, 16, 4, 20, 18, 9, 12, 3, 14, 15, 13, 101]
b=[13, 8, 20, 1, 15, 6, 10, 2, 6, 9, 8, 12, 18, 16, 5, 101]
c=[7, 18, 1, 10, 6, 3, 19, 7, 12, 20, 3, 6, 11, 7, 3, 101]
d=[]

for i in  a:
    if check(i,c)==2: d.append(i)
for i in b:
    if check(i,c)==2: d.append(i)

bubbleSort(a)
bubbleSort(b)
bubbleSort(c)
bubbleSort(d)

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

#Runtime of the program is 0.0009646415710449219