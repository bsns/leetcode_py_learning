# 给你一个整数数组 nums ，请你找出数组中乘积最大的非空连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。
#
#  测试用例的答案是一个 32-位 整数。
#
#
#
#  示例 1:
#
#
# 输入: nums = [2,3,-2,4]
# 输出: 6
# 解释: 子数组 [2,3] 有最大乘积 6。
#
#
#  示例 2:
#
#
# 输入: nums = [-2,0,-1]
# 输出: 0
# 解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。
#
#
#
#  提示:
#
#
#  1 <= nums.length <= 2 * 10⁴
#  -10 <= nums[i] <= 10
#  nums 的任何前缀或后缀的乘积都 保证 是一个 32-位 整数
#
#
#  Related Topics 数组 动态规划 👍 2251 👎 0

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)

        dp = [[0, 0] for _ in range(n)]

        dp[0][0] = nums[0]
        dp[0][1] = nums[0]
        max_res = nums[0]

        for i in range(1, n):
            dp[i][0] = min(dp[i - 1][0] * nums[i], dp[i - 1][1] * nums[i], nums[i])
            dp[i][1] = max(dp[i - 1][0] * nums[i], dp[i - 1][1] * nums[i], nums[i])

            max_res = max(max_res,dp[i][1])
        return max_res



Solution_demo = Solution()

# arr = [2,3,-2,4]

arr = [3,-1,4]

# 测试用例:[3,-1,4]
# 	测试结果:3
# 	期望结果:4
res = Solution_demo.maxProduct(arr)
print(res)