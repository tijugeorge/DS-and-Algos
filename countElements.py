class Solution:
    def countElements(self, arr: List[int]) -> int:
        dicti = {}
        for i in arr:
            if i in dicti:
                dicti[i]+= 1
            else:
                dicti[i] = 1
        count = 0
        for i in arr:
            if (i+1) in dicti:
                count += 1
        return count
