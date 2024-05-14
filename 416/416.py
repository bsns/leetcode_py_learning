# 给你一个 只包含正整数 的 非空 数组 nums 。请你判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。
#
#
#
#  示例 1：
#
#
# 输入：nums = [1,5,11,5]
# 输出：true
# 解释：数组可以分割成 [1, 5, 5] 和 [11] 。
#
#  示例 2：
#
#
# 输入：nums = [1,2,3,5]
# 输出：false
# 解释：数组不能分割成两个元素和相等的子集。
#
#
#
#
#  提示：
#
#
#  1 <= nums.length <= 200
#  1 <= nums[i] <= 100
#
#
#  Related Topics 数组 动态规划 👍 2072 👎 0
import time
from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # nums = [1, 5, 11, 5]

        total = sum(nums)
        target = total//2
        if total % 2 != 0:
            return False
        dp = [[False for _ in range(0,target+1) ] for _ in range(0,len(nums) + 1)]

        for i in range(len(nums) + 1):
            dp[i][0] = True

        for i in range(1,len(nums)+1):
            for j in range(1,target+1):
                # print(i,j,j-nums[i])
                if nums[i-1] > j:
                    dp[i][j]= dp[i-1][j]
                else:
                    dp[i][j] = max(dp[i-1][j],  dp[i-1][j-nums[i-1]])

        # for row in dp:
        #     print(row)

        return dp[len(nums)][target]


Solution_demo = Solution()
nums = [1,5,11,5]
res = Solution_demo.canPartition(nums)
print(res)