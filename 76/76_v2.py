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
#  Related Topics 哈希表 字符串 滑动窗口 👍 2883 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import defaultdict
        need = defaultdict(int)
        windows = defaultdict(int)

        left,right,min_length = 0,0,float('inf')

        for c in t:
            need[c] +=1
        flag = 0
        while(right<len(s)):
            c = s[right]
            right+=1
            if c in need:
                windows[c]+=1
                if windows[c] ==need[c]:
                    flag+=1

            while(flag == len(need)):
                if right -left <min_length:
                    start = left
                    min_length = right -left

                d = s[left]
                left+=1
                if d in need:
                    if windows[d] == need[d]:
                        flag-=1
                    windows[d]-=1

        return "" if min_length == float('inf') else s[start:start + min_length]

Solution_demo = Solution()
# 输入：s = "ADOBECODEBANC", t = "ABC"
# 输出："BANC"

s = "ADOBECODEBANC"
t = "ABC"
res = Solution_demo.minWindow(s,t)
print(res)
