# 给定两个整数 n 和 k，返回范围 [1, n] 中所有可能的 k 个数的组合。
#
#  你可以按 任何顺序 返回答案。
#
#
#
#  示例 1：
#
#
# 输入：n = 4, k = 2
# 输出：
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ]
#
#  示例 2：
#
#
# 输入：n = 1, k = 1
# 输出：[[1]]
#
#
#
#  提示：
#
#
#  1 <= n <= 20
#  1 <= k <= n
#
#
#  Related Topics 回溯 👍 1616 👎 0

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        def helper(n,start,res,tmp):
            if len(tmp) == k:
                res.append(tmp[:])
                return

            # res.append(tmp[:])
            for i in range(start,n):
                tmp.append(i+1)
                helper(n,i+1,res,tmp)
                tmp.pop()



        res = []
        helper(n,0,res,[])
        return res


Solution_sample = Solution()
# n = 4
# k = 2

n=1
k=1
res = Solution_sample.combine(n,k)
print(res)