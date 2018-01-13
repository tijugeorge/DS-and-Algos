def bubblesort(alist):
  for num in range(len(alist)-1, 0, -1):
    for i in range(num):
      if alist[i] > alist[i+1]:
        alist[i], alist[i+1] = alist[i+1], alist[i]
  return alist  
  
  
alist = [54,26,93,17,77,31,44,55,20]

print(bubblesort(alist))
