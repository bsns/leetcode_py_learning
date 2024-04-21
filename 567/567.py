# 给你两个字符串 s1 和 s2 ，写一个函数来判断 s2 是否包含 s1 的排列。如果是，返回 true ；否则，返回 false 。
#
#  换句话说，s1 的排列之一是 s2 的 子串 。
#
#
#
#  示例 1：
#
#
# 输入：s1 = "ab" s2 = "eidbaooo"
# 输出：true
# 解释：s2 包含 s1 的排列之一 ("ba").
#
#
#  示例 2：
#
#
# 输入：s1= "ab" s2 = "eidboaoo"
# 输出：false
#
#
#
#
#  提示：
#
#
#  1 <= s1.length, s2.length <= 10⁴
#  s1 和 s2 仅包含小写字母
#
#
#  Related Topics 哈希表 双指针 字符串 滑动窗口 👍 1000 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        # 给你两个字符串 s1 和 s2 ，写一个函数来判断 s2 是否包含 s1 的排列。如果是，返回 true ；否则，返回 false 。
        #
        #  换句话说，s1 的排列之一是 s2 的 子串 。
        #
        #
        #
        #  示例 1：
        #
        #
        # 输入：s1 = "ab" s2 = "eidbaooo"
        # 输出：true
        # 解释：s2 包含 s1 的排列之一 ("ba").
        #
        #
        #  示例 2：
        #
        #
        # 输入：s1= "ab" s2 = "eidboaoo"
        # 输出：false
        #
        #
        #
        #
        #  提示：
        #
        #
        #  1 <= s1.length, s2.length <= 10⁴
        #  s1 和 s2 仅包含小写字母
        #
        #
        #  Related Topics 哈希表 双指针 字符串 滑动窗口 👍 1000 👎 0



        from collections import defaultdict
        window = defaultdict(int)
        need = defaultdict(int)
        min_length = float('inf')
        # 输入：s1 = "ab" s2 = "eidbaooo"
        # 输出：true
        left, right = 0, 0
        flag = 0
        for c in s1:
            need[c] += 1

        while (right < len(s2)):

            d = s2[right]


            right += 1
            if d in need:
                window[d] += 1
                if window[d] == need[d]:
                    flag += 1

            while (right - left >= len(s1)):
                if flag == len(need):
                    return True

                d = s2[left]
                left += 1
                if d in need:
                    if window[d] == need[d]:
                        flag -= 1
                    window[d] -= 1
        return False


Solution_demo = Solution()
# s1 = "ab"
# s2 = "eidbaooo"
# # 期望结果: true

s1 = "hello"
s2 = "ooolleoooleh"

	# 期望结果:false

# s1 = "ab"
# s2 = "ab"
	# 期望结果:true
res = Solution_demo.checkInclusion(s1,s2)
print(res)
