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


        def circle(m,n,j,k):
            if m >n or j >k:
                return []
            elif(j == k):
                return matrix[j][m:n+1]
            elif(m == n):
                res = []
                for x in range(j,k+1):
                    res.append(matrix[x][m])
                return res
            else:
                res = []
                res.extend(matrix[j][m:n+1])
                for x in range(j+1,k):
                    res.append(matrix[x][n])
                res.extend(reversed(matrix[k][m:n+1]))
                for x in range(k-1,j,-1):
                    res.append(matrix[x][m])
                return res + circle(m+1,n-1,j+1,k-1)

        return  circle(0,len(matrix[0])-1,0,len(matrix) -1)


Solution_sample = Solution()

# matrix = [[1,2,3],[4,5,6],[7,8,9]]

#matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
matrix = [[1,2],[3,4]]
res = Solution_sample.spiralOrder(matrix)
print(res)
