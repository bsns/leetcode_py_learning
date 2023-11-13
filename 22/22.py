# 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
#
#
#
#  示例 1：
#
#
# 输入：n = 3
# 输出：["((()))","(()())","(())()","()(())","()()()"]
#
#
#  示例 2：
#
#
# 输入：n = 1
# 输出：["()"]
#
#
#
#
#  提示：
#
#
#  1 <= n <= 8
#
#
#  Related Topics 字符串 动态规划 回溯 👍 3434 👎 0

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        def dfs(cur_str,left,right,res):
            if left==0 and right==0:
                res.append(cur_str)
                return
            if right<left:
                return
            if left>0:
                dfs(cur_str+'(',left-1,right,res)
            if right>0:
                dfs(cur_str+')',left,right-1,res)




        cur_str = ''
        res = []

        dfs(cur_str,n,n,res)
        return res