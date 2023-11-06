# 给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。
#
#
#
#  注意：
#
#
#  对于 t 中重复字符，我们寻找的子字符串中该字符数量必须不少于 t 中该字符数量。
#  如果 s 中存在这样的子串，我们保证它是唯一的答案。
#
#
#
#
#  示例 1：
#
#
# 输入：s = "ADOBECODEBANC", t = "ABC"
# 输出："BANC"
# 解释：最小覆盖子串 "BANC" 包含来自字符串 t 的 'A'、'B' 和 'C'。
#
#
#  示例 2：
#
#
# 输入：s = "a", t = "a"
# 输出："a"
# 解释：整个字符串 s 是最小覆盖子串。
#
#
#  示例 3:
#
#
# 输入: s = "a", t = "aa"
# 输出: ""
# 解释: t 中两个字符 'a' 均应包含在 s 的子串中，
# 因此没有符合条件的子字符串，返回空字符串。
#
#
#
#  提示：
#
#
#  m == s.length
#  n == t.length
#  1 <= m, n <= 10⁵
#  s 和 t 由英文字母组成
#
#
#
# 进阶：你能设计一个在
# o(m+n) 时间内解决此问题的算法吗？
#
#  Related Topics 哈希表 字符串 滑动窗口 👍 2728 👎 0

import collections
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # 输入：s = "ADOBECODEBANC", t = "ABC"
        # 输出："BANC"

        need = collections.defaultdict(int)
        for c in t:
            need[c]+=1
        need_len = len(t)

        i_=0
        res = (0,float('inf'))

        for j,c in enumerate(s):
            if need[c]>0:
                need_len-=1
            need[c]-=1
            if need_len == 0:
                while True:
                    c = s[i_]
                    if need[c] ==0:
                        break
                    need[c]+=1
                    i_+=1
                if j-i_< res[1] -res[0]:
                    res =(i_,j)
                need[s[i_]]+=1
                need_len+=1
                i_ +=1
        return '' if res[1]>len(s) else s[res[0]:res[1]+1]









Solution_sample = Solution()
# s = "ADOBECODEBANC"
# t = "ABC"


# s = "a"
# t = "a"

# 测试用例:"a"
# 			"a"
# 	测试结果:""
# 	期望结果:"a"


# s = "aa"
# t = "aa"

# 测试用例:"aa"
# 			"aa"
# 	测试结果:""
# 	期望结果:"aa"

s = "abacaa"
t = "aa"

# a
#
# a:2
# b:1


res = Solution_sample.minWindow(s,t)
print(res)