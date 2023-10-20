# 给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。
#
#  注意：不能使用任何内置的 BigInteger 库或直接将输入转换为整数。
#
#
#
#  示例 1:
#
#
# 输入: num1 = "2", num2 = "3"
# 输出: "6"
#
#  示例 2:
#
#
# 输入: num1 = "123", num2 = "456"
# 输出: "56088"
#
#
#
#  提示：
#
#
#  1 <= num1.length, num2.length <= 200
#  num1 和 num2 只能由数字组成。
#  num1 和 num2 都不包含任何前导零，除了数字0本身。
#
#
#  Related Topics 数学 字符串 模拟 👍 1279 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # 输入: num1 = "123", num2 = "456"
        # 输出: "56088"

        # 18
        # 8
        #
        # 1
        #
        # 25+1 = 11
        m = len(num1)-1
        n = len(num2)-1
        #res = ''

        res = 0

        for i in range(m,-1 ,-1):
            stage = pow(10,m-i)

            for j in range(n,-1 ,-1):
                x = int(num1[i])
                y = int(num2[j])
                tmp_res = x*y

                res = tmp_res*stage + res
                stage = stage*10



        return str(res)

Solution_smaple = Solution()

num1 = "123"
num2 = "456"
# 输出: "56088"


num1 = "9"
num2 = "99"
# 测试用例:"9"
# 			"99"
# 	测试结果:"81"
# 	期望结果:"891"
res = Solution_smaple.multiply(num1,num2)
print(res)