#linear search
#list=[1,2, 16, 12, 18, 20]
##for i in range(len(list)):
#    if list[i]==item: print(list[i])


x=list(map(int, input().split()))
y=int(input())
o=0
for i in x: 
    if int(i)==y: o=1 
    break
if o==1: print('yes')
else: print('no')
