# 给你一个字符串 s，找到 s 中最长的回文子串。
#
#  如果字符串的反序与原始字符串相同，则该字符串称为回文字符串。
#
#
#
#  示例 1：
#
#
# 输入：s = "babad"
# 输出："bab"
# 解释："aba" 同样是符合题意的答案。
#
#
#  示例 2：
#
#
# 输入：s = "cbbd"
# 输出："bb"
#
#
#
#
#  提示：
#
#
#  1 <= s.length <= 1000
#  s 仅由数字和英文字母组成
#
#
#  Related Topics 字符串 动态规划 👍 6926 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        #s = "babad"
        #       11311
        #
        # s = "cbbd"
        #      1121
        #     "cbaabc"
        #      1112
        #      "cbadabc"
        #       1111345
        # dp = [0 for _ in range(len(s))]
        # for i in range(len(s)):
        n = len(s)

        dp = [[False for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i] =True

        max_len = 1
        start = 0
        for L in range(2,n+1):
            for i in range(n):
                j = i+L-1


                if j>n-1:
                    break

                if s[j] != s[i]:
                    dp[i][j] = False
                else:
                    if j-i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i+1][j-1]

                if dp[i][j] and j-i+1 > max_len:
                    max_len = j-i+1
                    start = i

        return s[start:start+max_len]


Solution_sample = Solution()
# s = "babad"

s = "cbbd"
# 测试用例:"cbbd"
# 	测试结果:"b"
# 	期望结果:"bb"

res = Solution_sample.longestPalindrome(s)
print(res)