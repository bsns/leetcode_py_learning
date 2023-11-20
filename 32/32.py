# 给你一个只包含 '(' 和 ')' 的字符串，找出最长有效（格式正确且连续）括号子串的长度。
#
#
#
#
#
#  示例 1：
#
#
#
#
# 输入：s = "(()"
# 输出：2
# 解释：最长有效括号子串是 "()"
#
#
#  示例 2：
#
#
# 输入：s = ")()())"
# 输出：4
# 解释：最长有效括号子串是 "()()"
#
#
#  示例 3：
#
#
# 输入：s = ""
# 输出：0
#
#
#
#
#  提示：
#
#
#  0 <= s.length <= 3 * 10⁴
#  s[i] 为 '(' 或 ')'
#
#
#  Related Topics 栈 字符串 动态规划 👍 2401 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # "(()"
        # ")(((())))"
        # ")(())"
        #  0002

        dp = [0 for _ in range(len(s))]

        res = 0
        start = 0
        for i in range(len(s)):
            if(i==3):
                print()
            tmp = s[i]
            if tmp =='(':
                dp[i] = 0
            else:
                if i>0 and s[i-1]=='(':
                    dp[i] = dp[i-2] +2

                elif(i>0)  and( i-dp[i-1] -1 >=0 )and( s[i-dp[i-1] -1] == '('):
                    dp[i] =dp[i-dp[i-1]-2] + dp[i-1] +2 # dp[i-1]

                res = max(dp[i],res)
        return res


Solution_smaple = Solution()
# s = "(()"

# s = ")()())"

# s = ")("

# s = "()(())"
	# 测试结果:2
	# 期望结果:6


s = "(()))())("
# 测试用例:"(()))())("
# 	测试结果:8
# 	期望结果:4
res = Solution_smaple.longestValidParentheses(s)
print(res)