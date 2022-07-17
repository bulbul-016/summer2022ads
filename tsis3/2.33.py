import time
start = time.time()

def quick_sort(s):
    if len(s)<2: return s

    pivot=s[len(s)-1]
    lower=list(filter(lambda x: x<pivot, s))
    center= [i for i in s if i==pivot]
    greater= list(filter(lambda x: x>pivot, s))

    return quick_sort(lower)+ center+ quick_sort(greater)

print(quick_sort([12,6,10,5,16,8,2,4]))
end = time.time()
print(f"Runtime of the program is {end - start}")