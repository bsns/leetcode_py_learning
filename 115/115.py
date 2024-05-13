# 给你两个字符串 s 和 t ，统计并返回在 s 的 子序列 中 t 出现的个数，结果需要对 10⁹ + 7 取模。
#
#
#
#  示例 1：
#
#
# 输入：s = "rabbbit", t = "rabbit"
# 输出：3
# 解释：
# 如下所示, 有 3 种可以从 s 中得到 "rabbit" 的方案。
# rabbbit
# rabbbit
# rabbbit
#
#  示例 2：
#
#
# 输入：s = "babgbag", t = "bag"
# 输出：5
# 解释：
# 如下所示, 有 5 种可以从 s 中得到 "bag" 的方案。
# babgbag
# babgbag
# babgbag
# babgbag
# babgbag
#
#
#
#
#  提示：
#
#
#  1 <= s.length, t.length <= 1000
#  s 和 t 由英文字母组成
#
#
#  Related Topics 字符串 动态规划 👍 1233 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # s = "rabbbit", t = "rabbit"
        # dp[i][j]  dp[i] 中 dp[j] 数量
        m = len(s)+1
        n = len(t)+1
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(0, m):
            dp[i][0] = 1
        for j in range(0, n):
            dp[0][j] = 0

        for i in range(1, m):
            for j in range(1, n):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[-1][-1]
Solution_demo = Solution()
s = "rabbbit"
t = "rabbit"
res = Solution_demo.numDistinct(s,t)
print(res)