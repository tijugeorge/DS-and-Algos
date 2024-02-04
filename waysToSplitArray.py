def waysToSplitArray(nums):
    n = len(nums)
    
    prefix = [nums[0]]
    for i in range(1, n):
        prefix.append(nums[i] + prefix[-1])

    ans = 0
    for i in range(n - 1):
        left_section = prefix[i]
        right_section = prefix[-1]- prefix[i]
        if left_section >= right_section:
            ans += 1

    return ans

nums = [1,2,3,4,5,6]
#nums = [10,4,-8,7]
print(waysToSplitArray(nums))
