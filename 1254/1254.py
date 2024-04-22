# 二维矩阵 grid 由 0 （土地）和 1 （水）组成。岛是由最大的4个方向连通的 0 组成的群，封闭岛是一个 完全 由1包围（左、上、右、下）的岛。
#
#  请返回 封闭岛屿 的数目。
#
#
#
#  示例 1：
#
#
#
#
# 输入：grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,
# 0,1],[1,1,1,1,1,1,1,0]]
# 输出：2
# 解释：
# 灰色区域的岛屿是封闭岛屿，因为这座岛屿完全被水域包围（即被 1 区域包围）。
#
#  示例 2：
#
#
#
#
# 输入：grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
# 输出：1
#
#
#  示例 3：
#
#
# 输入：grid = [[1,1,1,1,1,1,1],
#              [1,0,0,0,0,0,1],
#              [1,0,1,1,1,0,1],
#              [1,0,1,0,1,0,1],
#              [1,0,1,1,1,0,1],
#              [1,0,0,0,0,0,1],
#              [1,1,1,1,1,1,1]]
# 输出：2
#
#
#
#
#  提示：
#
#
#  1 <= grid.length, grid[0].length <= 100
#  0 <= grid[i][j] <=1
#
#
#  Related Topics 深度优先搜索 广度优先搜索 并查集 数组 矩阵 👍 293 👎 0

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:

        m = len(grid)
        n = len(grid[0])

        def dfs(grid, i, j):
            if i < 0 or i >= m or j < 0 or j >= n:
                return

            if grid[i][j] != 0:
                return
            grid[i][j] = -1
            dfs(grid, i - 1, j)
            dfs(grid, i, j - 1)
            dfs(grid, i + 1, j)
            dfs(grid, i, j + 1)

        for i in [0,m-1]:
            for j in range(0,n):
                dfs(grid,i,j)
        for i in range(0,m):
            for j in [0,n-1]:
                dfs(grid,i,j)

        res = 0
        for i in range(0,m):
            for j in range(0,n):
                if grid[i][j] == 0:
                    dfs(grid,i,j)
                    res+=1

        return  res


Solution_sample = Solution()


# grid = [[1,1,1,1,1,1,1],
#           [1,0,0,0,0,0,1],
#          [1,0,1,1,1,0,1],
#           [1,0,1,0,1,0,1],
#           [1,0,1,1,1,0,1],
#         [1,0,0,0,0,0,1],
#         [1,1,1,1,1,1,1]]
grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
# 期望结果:2
res = Solution_sample.closedIsland(grid)
print(res)