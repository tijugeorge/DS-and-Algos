def BubbleSortExample(list):
	for counter in range(len(list)-1, 0, -1):
		for i in range(counter):
			if list[i] < list[i+1]:
				list[i], list[i+1] = list[i+1], list[i]
	return list


list = [2,8,4,7,1,6,0,3,6,9,4,6,8,2]

print BubbleSortExample(list)
