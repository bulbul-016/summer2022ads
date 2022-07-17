def selectionsort(list1):

   for i in range(len(list1)-1,0,-1):
       pos_max=0
       for j in range(1,i+1):
           if list1[j]>list1[pos_max]:
               pos_max = j
       tmp = list1[i]
       print(tmp)
       list1[i] = list1[pos_max]
       print(list1)
       list1[pos_max] = tmp


list1 = [52,22,98,10,74,32,46,63,18]


selectionsort(list1)
print(list1)


