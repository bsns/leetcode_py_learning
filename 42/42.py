# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
#
#
#
#  示例 1：
#
#
#
#
# 输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
# 输出：6
# 解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。
#
#
#  示例 2：
#
#
# 输入：height = [4,2,0,3,2,5]
# 输出：9
#
#
#
#
#  提示：
#
#
#  n == height.length
#  1 <= n <= 2 * 10⁴
#  0 <= height[i] <= 10⁵
#
#
#  Related Topics 栈 数组 双指针 动态规划 单调栈 👍 4771 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def trap(self, height):
        #[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
        #简化  0,1,0,2

            # l  0 0 1 1
            #
            # r 2  2  2  0
            #   0  0  1

            n = len(height)
            left = [0 for _ in range(n+1)]
            right = [0 for _ in range(n+1)]

            l_max ,r_max = 0,0
            for i in range(0,n):
                left[i] = l_max
                l_max = max(l_max, height[i])

                right[n-i] = r_max
                r_max = max(r_max, height[n - i - 1])
            res = 0
            for j in range(0,n):
                cur = height[j]
                min_cur = min(left[j],right[j+1])
                if cur<min_cur:
                    res = res + min_cur -cur

            return res


Solution_smaple = Solution()

# height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

# height = [0, 1, 0, 2]


height = [4,2,0,3,2,5]

#0 2
# 测试结果:0
# 	期望结果:9
res = Solution_smaple.trap(height)
print(res)