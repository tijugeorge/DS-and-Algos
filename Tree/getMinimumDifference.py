class Solution:
    def getMinimumDifference(self, root):
        values = []
        def dfs(node):
            if not node:
                return 0
            #using inorder
            left = dfs(node.left)
            values.append(node.val)
            right = dfs(node.right)
            
        dfs(root)
        ans = float('inf')
        for i in range(1, len(values)):
            ans = min(ans, values[i]-values[i-1])
        return ans
