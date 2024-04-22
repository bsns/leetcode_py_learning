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
#  Related Topics 广度优先搜索 数组 动态规划 👍 2807 👎 0

from  typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # # 伪码框架
        # def coinChange(coins: List[int], amount: int) -> int:
        #     # 题目要求的最终结果是 dp(amount)
        #     return dp(coins, amount)
        #
        # # 定义：要凑出金额 n，至少要 dp(coins, n) 个硬币
        # def dp(coins: List[int], n: int) -> int:
        #     # 做选择，选择需要硬币最少的那个结果
        #     res = float('inf')  # 初始化res为正无穷
        #     for coin in coins:
        #         res = min(res, sub_problem + 1)
        #     return res

        if amount<0:
            return -1

        dp = [float('inf') for _ in range(amount+1)]
        dp[0] = 0

        for i in range(1,amount+1):
            for coin in coins:
                if i -coin<0:
                    continue
                dp[i] = min(dp[i],dp[i-coin]+1)

        if dp[amount] == float('inf'):
            return -1
        return dp[amount]


Solution_sample = Solution()

coins = [1, 2, 5]
amount = 11
res = Solution_sample.coinChange(coins,amount)
print(res)