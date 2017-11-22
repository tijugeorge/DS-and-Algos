#Lomuto partition scheme
def sortColors(nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    for i in range(len(nums)):
        start = i
        last = len(nums)-1
        while start < last:
            if nums[start] > nums[last]:
                nums[start], nums[last] = nums[last], nums[start]
            else:
                last -= 1
    return nums            



nums = [2,0,1]      
print(sortColors(nums))

#Hoare’s Partition Scheme
def sortColors(nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    
    ind0,ind1=0,0
    for i in range(len(nums)):
        a=nums[i] #assigning the current as max
        nums[i]=2
        if a<=1:  #if original is less than 2 then it should be 1
            nums[ind1]=1
            ind1+=1
        if a==0: #if original is less than 1 then it should be 0
            nums[ind0]=0
            ind0+=1
    return nums
            
nums = [2,0,1]      
print(sortColors(nums))
