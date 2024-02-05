def minStartValue(nums):
	start_value = 1
	while True:
		total = start_value
		isvalid = True 
		for num in nums:
			total+=num
			if total < 1:
				isvalid = False
				break
		if isvalid:
			return start_value
		else:
			start_value += 1
