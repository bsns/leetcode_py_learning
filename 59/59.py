# 给你一个正整数 n ，生成一个包含 1 到 n² 所有元素，且元素按顺时针顺序螺旋排列的 n x n 正方形矩阵 matrix 。
#
#
#
#  示例 1：
#
#
# 输入：n = 3
# 输出：[[1,2,3],[8,9,4],[7,6,5]]
#
#
#  示例 2：
#
#
# 输入：n = 1
# 输出：[[1]]
#
#
#
#
#  提示：
#
#
#  1 <= n <= 20
#
#
#  Related Topics 数组 矩阵 模拟 👍 1287 👎 0
from typing import List

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:


        res = [[0 for _ in range(n)] for _ in range(n )]
        top, bottom = 0, n-1
        left, right = 0, n-1
        cur = 1

        while (left <= right and top <= bottom):
            for i in range(left, right + 1):
                res[top][i] = cur
                cur += 1
            top += 1

            for j in range(top, bottom + 1):
                res[j][right] = cur
                cur += 1
            right -= 1
            for i in range(right, left - 1, -1):
                res[bottom][i] = cur
                cur += 1
            bottom -= 1

            for j in range(bottom, top - 1, -1):
                res[j][left] = cur
                cur += 1
            left += 1
        return res

Solution_demo = Solution()

n = 3
# 测试用例:3
# 	测试结果:[[1,2,3],[9,10,4],[7,6,5]]
# 	期望结果:[[1,2,3],[8,9,4],[7,6,5]]
res= Solution_demo.generateMatrix(n)

print(res)