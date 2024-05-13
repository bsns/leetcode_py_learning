# 给你一个字符串 s ，找出其中最长的回文子序列，并返回该序列的长度。
#
#  子序列定义为：不改变剩余字符顺序的情况下，删除某些字符或者不删除任何字符形成的一个序列。
#
#
#
#  示例 1：
#
#
# 输入：s = "bbbab"
# 输出：4
# 解释：一个可能的最长回文子序列为 "bbbb" 。
#
#
#  示例 2：
#
#
# 输入：s = "cbbd"
# 输出：2
# 解释：一个可能的最长回文子序列为 "bb" 。
#
#
#
#
#  提示：
#
#
#  1 <= s.length <= 1000
#  s 仅由小写英文字母组成
#
#
#  Related Topics 字符串 动态规划 👍 1203 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        # s = "bbbab"
        # 输出：4

        m = len(s)
        dp = [[0 for _ in range(m)] for _ in range(m)]
        for i in range(len(s)):
            dp[i][i] = 1
        for i in range(m,-1,-1):
            for j in range(i+1,m):
                if s[i] == s[j]:
                        dp[i][j] =  dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j] ,dp[i][j-1])

        return dp[0][-1]


Solution_demo  = Solution()
s = "cbbd"
res = Solution_demo.longestPalindromeSubseq(s)
print(res)