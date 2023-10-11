# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。
#
#  有效字符串需满足：
#
#
#  左括号必须用相同类型的右括号闭合。
#  左括号必须以正确的顺序闭合。
#  每个右括号都有一个对应的相同类型的左括号。
#
#
#
#
#  示例 1：
#
#
# 输入：s = "()"
# 输出：true
#
#
#  示例 2：
#
#
# 输入：s = "()[]{}"
# 输出：true
#
#
#  示例 3：
#
#
# 输入：s = "(]"
# 输出：false
#
#
#
#
#  提示：
#
#
#  1 <= s.length <= 10⁴
#  s 仅由括号 '()[]{}' 组成
#
#
#  Related Topics 栈 字符串 👍 4199 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isValid(self, s: str) -> bool:


        stack = ['?']
        stack.append(s[0])

        dic = {'(':')' , '[':']', '{':'}'}

        for tmp in range(1,len(s)):
            i = s[tmp]
            if i in ['(','[','{']:
                stack.append(i)

            else:
                if stack[-1] in dic:
                    if dic[ stack[-1]] == i:
                        stack.pop()
                    else:
                        stack.append(i)
                else:
                    stack.append(i)
        if  len(stack) == 1:
            return True
        else:
            return False

Solution_sample = Solution()
# s = "()[[]]{}"

s="()"
# 测试用例:"()"
# 	期望结果:true
#
#
# s = "(])"
# 测试用例:"(])"
# 	期望结果:false


# s = "(]"
# 测试用例:"(]"
# 期望结果:false

# s = "([)]"
# 测试用例:"([)]"

# s = "(){}}{"
# 期望结果:false
res = Solution_sample.isValid(s)
print(res)


