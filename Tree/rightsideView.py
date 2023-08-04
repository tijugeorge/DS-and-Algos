from collections import deque

class Solution:
    def rightsideView(self, root):
        if not root:
            return []
        
        ans = []
        queue = deque([root])
        
        while queue:
            current_length = len(queue)
            ans.append(queue[-1].val)
            
            for _ in range(current_length):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return ans
        
