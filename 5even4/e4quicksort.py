import time
start = time.time()

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
    
a=[15, 9, 10, 8, 7, 16, 4, 20, 18, 9, 12, 3, 14, 15, 13, 101]
b=[13, 8, 20, 1, 15, 6, 10, 2, 6, 9, 8, 12, 18, 16, 5, 101]
c=[7, 18, 1, 10, 6, 3, 19, 7, 12, 20, 3, 6, 11, 7, 3, 101]
d=[]

for i in  a:
    if check(i,c)==2: d.append(i)
for i in b:
    if check(i,c)==2: d.append(i)

quickSort(a, 0, len(a)-1)
quickSort(b, 0, len(b)-1)
quickSort(c, 0, len(c)-1)
quickSort(d, 0, len(d)-1)

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

#Runtime of the program is 0.002001523971557617