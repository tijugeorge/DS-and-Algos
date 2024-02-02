def findMaxAverage(nums, k):
    left = avg = curr = 0
    for i in range(k):
        curr += nums[i]
        #print('curr', curr)
    avg = curr/k
    #print(avg)
    for i in range(k, len(nums)):  #make k = 1 for another test case of curr
        try:
            #curr += (nums[i+k-1] - nums[left])
            curr += nums[i] - nums[i-k]
            #print('curr1', curr, nums[i+k], nums[left])
            #left += 1
        except IndexError:
            pass
        avg = max(avg, curr/k)
        #print('inside', avg)
        
    return avg
  

nums = [1,12,-5,-6,50,3]
k = 4
