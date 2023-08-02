matrix = [[1,3,5,7],
         [10,11,16,20],
         [23,30,34,60]]

class Solution:
    def searchMatrix(self, matrix, target):
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m*n-1
        
        while left <= right:
            mid = (left +right)//2
            row = mid//n
            col = mid%n
            num = matrix[row][col]
            
            if num==target:
                return row, col
            if num<target:
                left = mid+1
            else:
                right = mid-1
        return False    
SS=Solution()
print(SS.searchMatrix(matrix, 69))
