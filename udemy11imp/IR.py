#to check if an array is a rotation of other

def is_rotation(A, B):
	if len(A)!=len(B):
		return False
	first = A[0]
	key_index = -1
	for index in range(len(B)):
		if B[index] == first:
			key_index = index
			break
	if key_index == -1:
		return False

	for indexA in range(len(A)):
		indexB = (key_index+indexA)%len(A)
		if A[indexA]!=B[indexB]:
			return False
	return True


A = [1,2,3,4,5,6,7,8,9]
B = [5,6,7,8,9,1,2,3,4]

print(is_rotation(A, B))



