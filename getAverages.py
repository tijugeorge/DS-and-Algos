def getAverages(self, nums: List[int], k: int) -> List[int]:
    if k == 0:
        return nums
    windowsize = 2*k+1
    n = len(nums)
    averages = [-1]*n
    if windowsize > n:
        return averages
    prefix = [0]*(n+1)
    for i in range(n):
        prefix[i+1] = prefix[i]+nums[i]

    for i in range(k, n-k):
        lbound, rbound = i-k, i+k
        subarraysum = prefix[rbound+1]-prefix[lbound]
        average = subarraysum//windowsize   
        averages[i] = average
    return averages   
