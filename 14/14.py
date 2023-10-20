# 编写一个函数来查找字符串数组中的最长公共前缀。
#
#  如果不存在公共前缀，返回空字符串 ""。
#
#
#
#  示例 1：
#
#
# 输入：strs = ["flower","flow","flight"]
# 输出："fl"
#
#
#  示例 2：
#
#
# 输入：strs = ["dog","racecar","car"]
# 输出：""
# 解释：输入不存在公共前缀。
#
#
#
#  提示：
#
#
#  1 <= strs.length <= 200
#  0 <= strs[i].length <= 200
#  strs[i] 仅由小写英文字母组成
#
#
#  Related Topics 字典树 字符串 👍 2959 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestCommonPrefix(self, strs) -> str:

        res = 0
        for i in range(0,len(strs[0])):

            for j in range(0,len(strs)):
                if i>= len(strs[j]):
                    return strs[0][:res]

                elif strs[j][i] == strs[0][i]:
                    continue
                else:
                    return strs[0][:res]
            res += 1

        return strs[0][:res]


Solution_sample = Solution()

# strs = ["flower","flow","flight"]
strs = ["ab","a"]
res = Solution_sample.longestCommonPrefix(strs)
print(res)