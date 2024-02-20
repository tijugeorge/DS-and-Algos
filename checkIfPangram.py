class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        '''
        dic = {}
        if len(sentence) <26:
            return False
        for c in sentence:
            if c in dic:
                dic[c] += 1
            else:
                dic[c] = 1
        if len(dic) <26:
            return False
        return True
        '''
        seen = set(sentence)
        return len(seen) == 26
