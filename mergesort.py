def mergest(sortlist):
    print("Razbiyeniye ",sortlist)
    if len(sortlist)>1:
        m = len(sortlist)//2
        left = sortlist[:m]
        right = sortlist[m:]
        mergest(left)
        mergest(right)
        i=0
        j=0
        k=0
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                sortlist[k]=left[i]
                i+=1
            else:
                sortlist[k]=right[j]
                j+=1
            k+=1
        while i<len(left):
            sortlist[k]=left[i]
            i+=1
            k+=1
        while j<len(right):
            sortlist[k]=right[j]
            j+=1
            k+=1
    print("Sliyaniye ",sortlist)

list1 = [52,22,98,10,74,32,46,63,18]
mergest(list1)
print(list1)
