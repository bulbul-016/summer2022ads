def myMax(list1):
    maxnum = list1[0]
    for x in list1:
        if x > maxnum :
             maxnum = x
    return maxnum
 
list1 = [12,2,16,4,68,116,8]
print("Largest element is:", myMax(list1))
