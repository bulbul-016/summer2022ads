def counter(alist):
  if alist == []:
    return 0
  return 1 + counter(alist[1:])
  
print(counter([7,6,10,5,9,8,3,4]))