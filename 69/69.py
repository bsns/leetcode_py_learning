# 给你一个非负整数 x ，计算并返回 x 的 算术平方根 。
#
#  由于返回类型是整数，结果只保留 整数部分 ，小数部分将被 舍去 。
#
#  注意：不允许使用任何内置指数函数和算符，例如 pow(x, 0.5) 或者 x ** 0.5 。
#
#
#
#  示例 1：
#
#
# 输入：x = 4
# 输出：2
#
#
#  示例 2：
#
#
# 输入：x = 8
# 输出：2
# 解释：8 的算术平方根是 2.82842..., 由于返回类型是整数，小数部分将被舍去。
#
#
#
#
#  提示：
#
#
#  0 <= x <= 2³¹ - 1
#
#
#  Related Topics 数学 二分查找 👍 1457 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def mySqrt(self, x: int) -> int:

        left,right = 0,x

        mid = 0
        while(left <= right):
            mid = (right - left)//2 + left
            if mid*mid<= x  and (mid+1)*(mid+1) >x:
                return mid
            if(mid*mid< x):
                left = mid+1
            else:
                right =mid-1
        return mid

Solution_sample = Solution()
x = 8
res = Solution_sample.mySqrt(x)
print(res)