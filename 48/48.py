# 给定一个 n × n 的二维矩阵 matrix 表示一个图像。请你将图像顺时针旋转 90 度。
#
#  你必须在 原地 旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要 使用另一个矩阵来旋转图像。
#
#
#
#  示例 1：
#
#
# 输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
# 输出：[[7,4,1],[8,5,2],[9,6,3]]
#
#
#  示例 2：
#
#
# 输入：matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
# 输出：[[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
#
#
#
#
#  提示：
#
#
#  n == matrix.length == matrix[i].length
#  1 <= n <= 20
#  -1000 <= matrix[i][j] <= 1000
#
#
#
#
#  Related Topics 数组 数学 矩阵 👍 1641 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

        n = len(matrix)
        if n == 1:
            return

        def curRotate(k):


            #上行
            temp = matrix[k][k:n-k]

            #上行 赋值
            for i in range(k+1,n-k):
                #舍弃上行最右
                matrix[k][n-1-i] = matrix[i][k]
            #左列 赋值
            #舍弃 左列 当前行（第一行）
            for i in range(k+1,n-k):
                matrix[i][k] = matrix[n-1-k][i]
            #下行 赋值
            for i in range(k+1,n-k):
                # 舍弃下行最右
                matrix[n-1-k][n-1-i]=matrix[i][n - k - 1]

            for i in range(k, n - k):
                matrix[i][n - k - 1] = temp[i - k]

        start = 0
        while 2 * start + 1 < n:
            curRotate(start)
            start += 1

Solution_sample = Solution()
matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
res = Solution_sample.rotate(matrix)

for i in range(0,len(matrix)):
    print(matrix[i])
#print(res)