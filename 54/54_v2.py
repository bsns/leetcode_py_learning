# 给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。
#
#
#
#  示例 1：
#
#
# 输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
# 输出：[1,2,3,6,9,8,7,4,5]
#
#
#  示例 2：
#
#
# 输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# 输出：[1,2,3,4,8,12,11,10,9,5,6,7]
#
#
#
#
#  提示：
#
#
#  m == matrix.length
#  n == matrix[i].length
#  1 <= m, n <= 10
#  -100 <= matrix[i][j] <= 100
#
#
#  Related Topics 数组 矩阵 模拟 👍 1384 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        m = len(matrix)
        n = len(matrix[0])
        res = []
        top, bottom = 0, m - 1
        left, right = 0, n - 1
        cur = 1

        while (left <= right and top <= bottom):
            for i in range(left, right + 1):
                res.append(matrix[top][i])
                cur += 1
            top += 1
            if top>bottom:
                break
            for j in range(top, bottom + 1):
                res.append(matrix[j][right])
                cur += 1
            right -= 1
            if left>right:
                break
            for i in range(right, left - 1, -1):
                res.append(matrix[bottom][i])
                cur += 1
            bottom -= 1
            if top>bottom:
                break
            for j in range(bottom, top - 1, -1):
                res.append(matrix[j][left])
                cur += 1
            left += 1
            if left>right:
                break
        return res


Solution_sample = Solution()

# matrix = [[1,2,3],[4,5,6],[7,8,9]]

matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# 期望结果:[1,2,3,4,8,12,11,10,9,5,6,7]

# matrix = [[1,2],[3,4]]
res = Solution_sample.spiralOrder(matrix)
print(res)
