# 给定一个字符串 queryIP。如果是有效的 IPv4 地址，返回 "IPv4" ；如果是有效的 IPv6 地址，返回 "IPv6" ；如果不是上述类型的
# IP 地址，返回 "Neither" 。
#
#  有效的IPv4地址 是 “x1.x2.x3.x4” 形式的IP地址。 其中 0 <= xi <= 255 且 xi 不能包含 前导零。例如: “192.1
# 68.1.1” 、 “192.168.1.0” 为有效IPv4地址， “192.168.01.1” 为无效IPv4地址; “192.168.1.00” 、 “1
# 92.168@1.1” 为无效IPv4地址。
#
#  一个有效的IPv6地址 是一个格式为“x1:x2:x3:x4:x5:x6:x7:x8” 的IP地址，其中:
#
#
#  1 <= xi.length <= 4
#  xi 是一个 十六进制字符串 ，可以包含数字、小写英文字母( 'a' 到 'f' )和大写英文字母( 'A' 到 'F' )。
#  在 xi 中允许前导零。
#
#
#  例如 "2001:0db8:85a3:0000:0000:8a2e:0370:7334" 和 "2001:db8:85a3:0:0:8A2E:0370:7
# 334" 是有效的 IPv6 地址，而 "2001:0db8:85a3::8A2E:037j:7334" 和 "02001:0db8:85a3:0000:000
# 0:8a2e:0370:7334" 是无效的 IPv6 地址。
#
#
#
#  示例 1：
#
#
# 输入：queryIP = "172.16.254.1"
# 输出："IPv4"
# 解释：有效的 IPv4 地址，返回 "IPv4"
#
#
#  示例 2：
#
#
# 输入：queryIP = "2001:0db8:85a3:0:0:8A2E:0370:7334"
# 输出："IPv6"
# 解释：有效的 IPv6 地址，返回 "IPv6"
#
#
#  示例 3：
#
#
# 输入：queryIP = "256.256.256.256"
# 输出："Neither"
# 解释：既不是 IPv4 地址，又不是 IPv6 地址
#
#
#
#
#  提示：
#
#
#  queryIP 仅由英文字母，数字，字符 '.' 和 ':' 组成。
#
#
#  Related Topics 字符串 👍 248 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def validIPAddress(self, queryIP: str) -> str:

        path = queryIP.split('.')
        if len(path) == 4:
            for sub in path:
                if not sub or not sub.isdecimal():
                    return "Neither"
                if sub[0] == '0' and len(sub) != 1:
                    return "Neither"
                if int(sub) > 255:
                    return "Neither"

            return "IPv4"

        path = queryIP.split(':')
        if len(path) == 8:
            for sub in path:
                if not sub:
                    return "Neither"
                if len(sub) > 4:
                    return "Neither"
                for s in sub:
                    if not (('0' <= s <= '9') or ('a' <= s <= 'f') or ('A' <= s <= 'F')):
                        return "Neither"

            return "IPv6"

        return "Neither"

Solution_sample = Solution()
# queryIP = "172.16.254.1"

# 测试用例:"172.16.254.1"
# 	测试结果:"Neither"
#
# 	期望结果:"IPv4"

# queryIP = "2001:0db8:85a3:0:0:8A2E:0370:7334"
queryIP = "2001:0db8:85a3:00000:0:8A2E:0370:7334"

# 测试用例:"2001:0db8:85a3:0:0:8A2E:0370:7334"
# 	测试结果:"Neither"
# 	期望结果:"IPv6"


queryIP = "20EE:Fb8:85a3:0:0:8A2E:0370:7334"
# 测试用例:"20EE:Fb8:85a3:0:0:8A2E:0370:7334"
# 	测试结果:"Neither"
# 	期望结果:"IPv6"
res = Solution_sample.validIPAddress(queryIP)
print(res)