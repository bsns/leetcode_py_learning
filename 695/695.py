# 给你一个大小为 m x n 的二进制矩阵 grid 。
#
#  岛屿 是由一些相邻的 1 (代表土地) 构成的组合，这里的「相邻」要求两个 1 必须在 水平或者竖直的四个方向上 相邻。你可以假设 grid 的四个边缘都
# 被 0（代表水）包围着。
#
#  岛屿的面积是岛上值为 1 的单元格的数目。
#
#  计算并返回 grid 中最大的岛屿面积。如果没有岛屿，则返回面积为 0 。
#
#
#
#  示例 1：
#
#
# 输入：grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,
# 0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,
# 0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
# 输出：6
# 解释：答案不应该是 11 ，因为岛屿只能包含水平或垂直这四个方向上的 1 。
#
#
#  示例 2：
#
#
# 输入：grid = [[0,0,0,0,0,0,0,0]]
# 输出：0
#
#
#
#
#  提示：
#
#
#  m == grid.length
#  n == grid[i].length
#  1 <= m, n <= 50
#  grid[i][j] 为 0 或 1
#
#
#  Related Topics 深度优先搜索 广度优先搜索 并查集 数组 矩阵 👍 1021 👎 0
from typing import  List

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # 输入：grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        #              [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
        #              [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        #              [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
        # 输出：6
        self.max_area = 0
        def dfs(grid,i,j):

            res = 0
            if(0<=i<len(grid) and 0<=j<len(grid[0]) and grid[i][j] == 1):
                res += 1
                grid[i][j] = -1
                res = res + dfs(grid,i-1,j) + dfs(grid,i+1,j) + dfs(grid, i,j-1) + dfs(grid,i,j+1)

            if res > self.max_area :
                self.max_area = res
            return res


        for i in range(0,len(grid)):
            for j in range(0,len(grid[0])):
                if (grid[i][j] == 1):
                    dfs(grid,i,j)

        return self.max_area


Solution_sample = Solution()
grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
     [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
     [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
        # 输出：6

res = Solution_sample.maxAreaOfIsland(grid)
print(res)