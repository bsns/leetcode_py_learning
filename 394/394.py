# 给定一个经过编码的字符串，返回它解码后的字符串。
#
#  编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。
#
#  你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。
#
#  此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像 3a 或 2[4] 的输入。
#
#
#
#  示例 1：
#
#
# 输入：s = "3[a]2[bc]"
# 输出："aaabcbc"
#
#
#  示例 2：
#
#
# 输入：s = "3[a2[c]]"
# 输出："accaccacc"
#
#
#  示例 3：
#
#
# 输入：s = "2[abc]3[cd]ef"
# 输出："abcabccdcdcdef"
#
#
#  示例 4：
#
#
# 输入：s = "abc3[cd]xyz"
# 输出："abccdcdcdxyz"
#
#
#
#
#  提示：
#
#
#  1 <= s.length <= 30
#
#  s 由小写英文字母、数字和方括号
#  '[]' 组成
#  s 保证是一个 有效 的输入。
#  s 中所有整数的取值范围为
#  [1, 300]
#
#
#  Related Topics 栈 递归 字符串 👍 1616 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def decodeString(self, s: str) -> str:
        # 输入：s = "a3[a]2[bc]"
        # 输出："aaabcbc"
        # 示例
        n = len(s)
        stack = []
        res = ''
        tmp = ''
        multi = 0
        for c in s:
            if c == '[':
                stack.append([multi,res])
                multi = 0
                res = ''
            elif(c == ']'):
                last_m,last_res = stack.pop()
                res = last_res + last_m*res
            elif( '0'<= c <= '9'):
                multi = multi*10 + int(c)
            else:
                res += c
        return res



        # for i in range(0,n):
        #     if( 'a'<=s[i]<='z' and len(stack) ==0 ):
        #        res = res + s[i]
        #     elif( s[i] == '[' or ('a'<=s[i]<='z' and len(stack) >0 ) or ('0' <= s[i] <= '9') ):
        #         stack.append(s[i])
        #     else:
        #
        #         # tmp = ''
        #         while(len(stack)>0 and stack[-1]!= '['):
        #             tmp = stack.pop() + tmp
        #         stack.pop()
        #
        #         times = ''
        #         while (len(stack) > 0 and '0' <= stack[-1] <= '9'):
        #             times = stack.pop() + times
        #         times = int(times)
        #
        #         if len(stack) == 0:
        #             res = res + times*tmp
        #             tmp = ''
        #         else:
        #             tmp = times*tmp
        return res






Solution_sample = Solution()

s = "3[a]2[bc]"
#
# s = "3[a2[c]]"
      # 3 acc
# 测试用例:"3[a2[c]]"
# 	期望结果:"accaccacc"



#

#
# s = "3[z]2[2[y]pq4[2[jk]e1[f]]]ef"
	# 测试结果:"zzzpqefjkyyjkyyefjkyyjkyyefjkyyjkyyefjkyyjkyypqefjkyyjkyyefjkyyjkyyefjkyyjkyyefjkyyjkyyef"
	# 期望结果:"zzzyypqjkjkefjkjkefjkjkefjkjkefyypqjkjkefjkjkefjkjkefjkjkefef"
res = Solution_sample.decodeString(s)
print(res)

# assert res == "zzzyypqjkjkefjkjkefjkjkefjkjkefyypqjkjkefjkjkefjkjkefjkjkefef"