def numsubarrayProductlessthanK(nums, k):    #product less thn k
	if k<=1:
		return 0

	ans =left = 0
	curr= 1
	for right in range(len(nums)):
		curr *= nums[right]
		while curr >= k:
			curr //= nums[left]
			left += 1
		ans += right -left +1
	return ans
nums = [10,5,2,6]
k = 100
print(numsubarrayProductlessthanK(nums, k))

nums = [3,-1,4,12,-8,5,6]
k = 4

def find_best_subarray(nums, k):
	curr = 0 
	for i in range(k):
		curr += nums[i]

	ans  = curr 
	for i in range(k, len(nums)):
		curr += nums[i] - nums[i-k]
		ans = max(ans, curr)

	return ans

print(find_best_subarray(nums, k))
