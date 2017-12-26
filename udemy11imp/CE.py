# find common elements

def commonElements(list1, list2):
	p1, p2 = 0, 0
	result = []
	while p1 < len(list1) and p2 < len(list2):
		if list1[p1] == list2[p2]:
			result.append(list1[p1])
			p1+=1
			p2+=1
		elif list1[p1] < list2[p2]:
			p1+=1
		else:
			p2+=1 
	return result


list1 = [1,2,4,5,7,9]
list2 = [2,3,4,6,7]

print(commonElements(list1, list2))
