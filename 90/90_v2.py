# 给你一个整数数组 nums ，其中可能包含重复元素，请你返回该数组所有可能的 子集（幂集）。
#
#  解集 不能 包含重复的子集。返回的解集中，子集可以按 任意顺序 排列。
#
#
#
#
#
#
#
#  示例 1：
#
#
# 输入：nums = [1,2,2]
# 输出：[[],[1],[1,2],[1,2,2],[2],[2,2]]
#
#
#  示例 2：
#
#
# 输入：nums = [0]
# 输出：[[],[0]]
#
#
#
#
#  提示：
#
#
#  1 <= nums.length <= 10
#  -10 <= nums[i] <= 10
#
#
#  Related Topics 位运算 数组 回溯 👍 1205 👎 0
from typing import List

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def backtrack(nums, start, res, tmp):
            res.append(tmp[:])

            for i in range(start, len(nums)):
                if(i > start and nums[i] == nums[i-1]):
                    continue

                tmp.append(nums[i])
                backtrack(nums, i + 1, res, tmp)
                tmp.pop()

        nums.sort()
        res = []
        backtrack(nums, 0, res, [])
        return res


Solution_sample = Solution()

# nums = [1,2,2]

nums = [4,4,4,1,4]

期望结果:[[],[1],[1,4],[1,4,4],[1,4,4,4],[1,4,4,4,4],[4],[4,4],[4,4,4],[4,4,4,4]]

res = Solution_sample.subsetsWithDup(nums)
print(res)