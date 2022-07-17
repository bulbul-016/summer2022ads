def quick_sort(olist):
    if len(olist) <= 1: return olist
    else: pivot = olist.pop()
    greater = []
    lower = []
    for item in olist:
        if item > pivot:
            greater.append(item)
        else:
            lower.append(item)
    return quick_sort(lower) + [pivot] + quick_sort(greater)


print(quick_sort([5,6,7,8,9,8,7,6,5,6,7,8,9,0]))
