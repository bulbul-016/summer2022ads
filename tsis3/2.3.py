import random
import time

start = time.time()
def quick_sort(s):
    if len(s)<2: return s

    pivot=s[0]
    #print(pivot)
    lower=list(filter(lambda x: x<pivot, s))
    center= [i for i in s if i==pivot]
    greater= list(filter(lambda x: x>pivot, s))
    #print(lower)
    return quick_sort(lower)+ center+ quick_sort(greater)

print(quick_sort([55,48,378,115,63,9,81,3,49]))
end = time.time()
print(f"Runtime of the program is {end - start}")

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

import time
start = time.time()
def quick_sort(s):
    if len(s)<2: return s

    pivot=s[len(s)//2]
    lower=list(filter(lambda x: x<pivot, s))
    center= [i for i in s if i==pivot]
    greater= list(filter(lambda x: x>pivot, s))

    return quick_sort(lower)+ center+ quick_sort(greater)

print(quick_sort([26,2,116,98,72,50,667]))
end = time.time()
print(f"Runtime of the program is {end - start}")


import time
start = time.time()
def quick_sort(s):
    if len(s)<2: return s

    pivot=s[random.randint(0, len(s)-1)]
   # print(pivot)
    lower=list(filter(lambda x: x<pivot, s))
    center= [i for i in s if i==pivot]
    greater= list(filter(lambda x: x>pivot, s))
    #print(lower)
    #print(center)
    #print(greater)
    return quick_sort(lower)+ center+ quick_sort(greater)

print(quick_sort([19,65,25,5,34,8,3,4]))
end = time.time()
print(f"Runtime of the program is {end - start}")