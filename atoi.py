
def atoi(string):
  res = 0
  for i in range(len(string)):
    res = res*10 + (ord(string[i])-ord('0'))
  return res
    
    
print(atoi('989898'))
