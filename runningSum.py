def runningSum(nums):
	res = [nums[0]]
	for i in range(1, len(nums)):
		res.append(res[-1]+nums[i])
	return res
	#OR      above space complexity is O(n) and beloww it  is O(1)
	for i in range(len(nums)):
		nums[i] += nums[i-1]
	return nums
