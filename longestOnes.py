def longestOnes(nums, k):
	left = 0
	for right in range(len(nums)):
		k -= 1-nums[right]
		if k<0:
			k += 1-nums[left]
			left += 1
	return right - left +1




nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2


nums= [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
k = 3
print(longestOnes(nums, k))
