def non_repeating(string):
  counter = {}
  for c in string:
    if c not in counter:
      counter[c] = 1
    else:
      counter[c]+=1
  for c in string:
    if counter[c]==1:
      return c
  return None
  
  
print(non_repeating("abcab")) # should return 'c'
print(non_repeating("abab")) # should return None
print(non_repeating("aabbbc")) # should return 'c'
print(non_repeating("aabbdbc")) # should return 'd'
