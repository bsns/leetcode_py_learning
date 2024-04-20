# 给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。
#
#
#
#  示例 1：
#
#
# 输入：nums = [1,2,3]
# 输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
#
#
#  示例 2：
#
#
# 输入：nums = [0,1]
# 输出：[[0,1],[1,0]]
#
#
#  示例 3：
#
#
# 输入：nums = [1]
# 输出：[[1]]
#
#
#
#
#  提示：
#
#
#  1 <= nums.length <= 6
#  -10 <= nums[i] <= 10
#  nums 中的所有整数 互不相同
#
#
#  Related Topics 数组 回溯 👍 2872 👎 0
from typing import List

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        res = []
        def help(res,tmp,used):
            if len(tmp) == len(nums):
                res.append(tmp[:])
                return

            for i in range(0,len(nums)):
                if used[i]:
                    continue
                tmp.append(nums[i])
                used[i] = True
                help(res,tmp,used)
                tmp.pop()
                used[i] =False

        used = [False for _ in range(len(nums))]

        help(res,[],used)

        return res


Solution_sample = Solution()
nums = [1,2,3]
# 期望结果:[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
res = Solution_sample.permute(nums)
print(nums)