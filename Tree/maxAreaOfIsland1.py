class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        seen = set()
        ans = 0
        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                if val and (i, j) not in seen:
                    shape = 0
                    stack = [(i, j)]
                    seen.add((i,j))
                    while stack:
                        r, c = stack.pop()
                        shape+=1
                        for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
                            if (0<=nr<len(grid) and 0<=nc<len(grid[0]) and grid[nr][nc] and (nr, nc) not in seen):
                                stack.append((nr, nc))
                                seen.add((nr, nc))
                    ans = max(ans, shape)
        return ans
