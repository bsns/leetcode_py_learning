# 给你一个满足下述两条属性的 m x n 整数矩阵：
#
#
#  每行中的整数从左到右按非严格递增顺序排列。
#  每行的第一个整数大于前一行的最后一个整数。
#
#
#  给你一个整数 target ，如果 target 在矩阵中，返回 true ；否则，返回 false 。
#
#
#
#  示例 1：
#
#
# 输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# 输出：true
#
#
#  示例 2：
#
#
# 输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# 输出：false
#
#
#
#
#  提示：
#
#
#  m == matrix.length
#  n == matrix[i].length
#  1 <= m, n <= 100
#  -10⁴ <= matrix[i][j], target <= 10⁴
#
#
#  Related Topics 数组 二分查找 矩阵 👍 919 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

            line = 0
            while(line>=0 and line<len(matrix)):
                if matrix[line][-1]>=target:
                    break
                else:
                    line+=1
            if line>=len(matrix):
                return False

            for i in range(0,len(matrix[0])):
                if matrix[line][i] == target:
                    return True
            return False
