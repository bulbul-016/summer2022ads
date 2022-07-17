import time
start = time.time()

def selectionsort(list1):
    for i in range(len(list1)-1,0,-1):
       pos_max=0
       for j in range(1,i+1):
           if list1[j]>list1[pos_max]:
               pos_max = j
       tmp = list1[i]
       list1[i] = list1[pos_max]
       list1[pos_max] = tmp


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

selectionsort(a)
selectionsort(b)
selectionsort(c)
selectionsort(d)

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