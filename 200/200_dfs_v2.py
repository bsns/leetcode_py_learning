# 给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
#
#  岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。
#
#  此外，你可以假设该网格的四条边均被水包围。
#
#
#
#  示例 1：
#
#
# 输入：grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# 输出：1
#
#
#  示例 2：
#
#
# 输入：grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# 输出：3
#
#
#
#
#  提示：
#
#
#  m == grid.length
#  n == grid[i].length
#  1 <= m, n <= 300
#  grid[i][j] 的值为 '0' 或 '1'
#
#
#  Related Topics 深度优先搜索 广度优先搜索 并查集 数组 矩阵 👍 2472 👎 0

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        m = len(grid)
        n = len(grid[0])


        def dfs(grid,i,j):
            if i<0 or i>=m or j<0 or j>=n:
                return

            if grid[i][j] != '1':
                return
            grid[i][j] ='-1'
            dfs(grid,i-1,j)
            dfs(grid,i,j-1)
            dfs(grid, i+1, j)
            dfs(grid, i, j+1)

        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    dfs(grid,i,j)
                    res+=1
        return res


Solution_sample = Solution()
# grid = [ ["1","1","1","1","0"], ["1","1","0","1","0"], ["1","1","0","0","0"], ["0","0","0","0","0"] ]


grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
res = Solution_sample.numIslands(grid)
print(res)