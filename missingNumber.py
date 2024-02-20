    def missingNumber(self, nums: List[int]) -> int:
        num = set(nums)
        l = len(nums)+1
        dic = {}
        for i in range(l):
            if i not in num:
                return i
