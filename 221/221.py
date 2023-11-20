# 在一个由 '0' 和 '1' 组成的二维矩阵内，找到只包含 '1' 的最大正方形，并返回其面积。
#
#
#
#  示例 1：
#
#
# 输入：matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"]
# ,["1","0","0","1","0"]]
# 输出：4
#
#
#  示例 2：
#
#
# 输入：matrix = [["0","1"],["1","0"]]
# 输出：1
#
#
#  示例 3：
#
#
# 输入：matrix = [["0"]]
# 输出：0
#
#
#
#
#  提示：
#
#
#  m == matrix.length
#  n == matrix[i].length
#  1 <= m, n <= 300
#  matrix[i][j] 为 '0' 或 '1'
#
#
#  Related Topics 数组 动态规划 矩阵 👍 1583 👎 0


from  typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])

        dp = [[0 for _ in range(n)] for _ in range(m)]

        res = 0
        for i in range(m):
            for j in range(n):
                if int(matrix[i][j]) ==1:
                    if i==0 and j==0 :
                        dp[i][i] = int(matrix[i][j])
                    elif(i ==0):
                        dp[i][j] = (int(matrix[i][j]) ) #and dp[i][j-1])
                    elif(j == 0):
                        dp[i][j] = (int(matrix[i][j]))  ##and dp[i-1][j])
                    else:
                        dp[i][j] = min(dp[i-1][j-1] ,dp[i-1][j], dp[i][j-1]) + int(matrix[i][j])

                    res = max(res, dp[i][j]*dp[i][j])#dp[i-1][j-1]*dp[i-1][j-1])
        return res

Solution_sample = Solution()
# matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]

#matrix = [["0","1"],["1","0"]]

#matrix = [["0","1"]]


matrix = [["1","0","1","1","0","1"],["1","1","1","1","1","1"],["0","1","1","0","1","1"],["1","1","1","0","1","0"],["0","1","1","1","1","1"],["1","1","0","1","1","1"]]
	# 测试结果:9
	# 期望结果:4

# [["1","0","1","1","0","1"]
#  ["1","1","1","1","1","1"]
#  ["0","1","1","0","1","1"]
#  ["1","1","1","0","1","0"]
#  ["0","1","1","1","1","1"]
#  ["1","1","0","1","1","1"]]

res = Solution_sample.maximalSquare(matrix)
print(res)
