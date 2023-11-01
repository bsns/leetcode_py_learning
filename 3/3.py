# 给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。
#
#
#
#  示例 1:
#
#
# 输入: s = "abcabcbb"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
#
#
#  示例 2:
#
#
# 输入: s = "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
#
#
#  示例 3:
#
#
# 输入: s = "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
#      请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
#
#
#
#
#  提示：
#
#
#  0 <= s.length <= 5 * 10⁴
#  s 由英文字母、数字、符号和空格组成
#
#
#  Related Topics 哈希表 字符串 滑动窗口 👍 9757 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
# leetcode submit region end(Prohibit modification and deletion)
# s = "abcabcbb"

        n = len(s)
        max_res = 0
        max_keeper = 0
        recoder_s = ''
# s = "aabaab!bb"
        for i in range(0,n):
            tmp = s[i]

            if tmp not in recoder_s:
                # recoder[tmp] = i
                max_keeper +=1
                recoder_s +=tmp
                max_res = max(max_res,max_keeper)
            else:
                exist_idx = recoder_s.index(tmp)
                max_keeper = len(recoder_s) - exist_idx
                recoder_s = recoder_s[exist_idx+1:] + tmp

        return max_res


Solution_sample = Solution()
# s = "abcabcbb"
# s = "bbbbb"
s = "aabaab!bb"
# 测试用例:"aabaab!bb"
# 	测试结果:2
# 	期望结果:3
res = Solution_sample.lengthOfLongestSubstring(s)
print(res)