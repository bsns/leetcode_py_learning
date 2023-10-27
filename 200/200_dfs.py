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
#  Related Topics 深度优先搜索 广度优先搜索 并查集 数组 矩阵 👍 2338 👎 0

from typing import  List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(grid,i,j):
            if not (0<=i<len(grid)  and 0<=j<len(grid[0]) and grid[i][j] == "1"):
                return
            grid[i][j] = "0"
            dfs(grid,i-1,j)
            dfs(grid,i+1,j)
            dfs(grid,i,j-1)
            dfs(grid,i,j+1)

        count = 0

        for i in range(0,len(grid)):
            for j in range(0,len(grid[0])):
                if (grid[i][j] == '1'):
                    dfs(grid,i,j)
                    count+=1
        return count


Solution_sample = Solution()
grid = [ ["1","1","1","1","0"], ["1","1","0","1","0"], ["1","1","0","0","0"], ["0","0","0","0","0"] ]
res = Solution_sample.numIslands(grid)
print(res)