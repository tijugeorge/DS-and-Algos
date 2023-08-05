# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return []
        queue = deque([root])
        ans = []
        
        while queue:
            current_length = len(queue)
            curr_level_total = 0
            total = 0
            for _ in range(current_length):
                node = queue.popleft()
                total += node.val
                curr_level_total = total
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return curr_level_total
