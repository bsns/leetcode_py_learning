# 给你一个整数数组 coins ，表示不同面额的硬币；以及一个整数 amount ，表示总金额。
#
#  计算并返回可以凑成总金额所需的 最少的硬币个数 。如果没有任何一种硬币组合能组成总金额，返回 -1 。
#
#  你可以认为每种硬币的数量是无限的。
#
#
#
#  示例 1：
#
#
# 输入：coins = [1, 2, 5], amount = 11
# 输出：3
# 解释：11 = 5 + 5 + 1
#
#  示例 2：
#
#
# 输入：coins = [2], amount = 3
# 输出：-1
#
#  示例 3：
#
#
# 输入：coins = [1], amount = 0
# 输出：0
#
#
#
#
#  提示：
#
#
#  1 <= coins.length <= 12
#  1 <= coins[i] <= 2³¹ - 1
#  0 <= amount <= 10⁴
#
#
#  Related Topics 广度优先搜索 数组 动态规划 👍 2626 👎 0

from typing import  List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:


        def dp(amount):
            res = float('INF')

            if amount < 0 :
                return -1
            if amount == 0:
                return 0

            for coin in coins:
                sub_dp = dp(amount-coin)

                if sub_dp == -1:
                    continue
                res = min(res, 1+sub_dp)
            return res if res != float('inf') else -1



        return dp(amount)

Solution_sample = Solution()

coins = [1, 2, 5]
amount = 11
res = Solution_sample.coinChange(coins,amount)
print(res)