# 给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和并同样以字符串形式返回。
#
#  你不能使用任何內建的用于处理大整数的库（比如 BigInteger）， 也不能直接将输入的字符串转换为整数形式。
#
#
#
#  示例 1：
#
#
# 输入：num1 = "11", num2 = "123"
# 输出："134"
#
#
#  示例 2：
#
#
# 输入：num1 = "456", num2 = "77"
# 输出："533"
#
#
#  示例 3：
#
#
# 输入：num1 = "0", num2 = "0"
# 输出："0"
#
#
#
#
#
#
#  提示：
#
#
#  1 <= num1.length, num2.length <= 10⁴
#  num1 和num2 都只包含数字 0-9
#  num1 和num2 都不包含任何前导零
#
#
#  Related Topics 数学 字符串 模拟 👍 796 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:


        m = len(num1)-1
        n = len(num2)-1

        tmp = 0
        res = ''
        while(m>=0 or n>=0 ):

            if (m<0 and n<0 and tmp >0):
                tmp_sum = tmp
            elif m < 0:
                tmp_sum =  int(num2[n]) + tmp
            elif(n < 0):
                tmp_sum = int(num1[m])  + tmp

            else:
                tmp_sum = int(num1[m]) + int(num2[n]) + tmp
            if tmp_sum>9:
                tmp = 1
                tmp_sum = tmp_sum - 10
            else:
                tmp = 0
            m-=1
            n-=1
            res = str(tmp_sum)+ res

        if(tmp>0):
            res = str(tmp) + res
        return res

Solution_sample = Solution()

num1 = "11"
num2 = "123"
# 输出："134"


num1 = "456"
num2 = "77"
	# 期望结果:"533"


num1 = "1"
num2 = "9"
	# 期望结果:"10"
res = Solution_sample.addStrings(num1,num2)
print(res)