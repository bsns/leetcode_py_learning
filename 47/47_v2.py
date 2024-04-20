# 给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。
#
#
#
#  示例 1：
#
#
# 输入：nums = [1,1,2]
# 输出：
# [[1,1,2],
#  [1,2,1],
#  [2,1,1]]
#
#
#  示例 2：
#
#
# 输入：nums = [1,2,3]
# 输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
#
#
#
#
#  提示：
#
#
#  1 <= nums.length <= 8
#  -10 <= nums[i] <= 10
#
#
#  Related Topics 数组 回溯 👍 1562 👎 0
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrack(nums, start, res, tmp, used):
            if(len(tmp) == len(nums)):
                res.append(tmp[:])
                return

            for i in range(0, len(nums)):
                if used[i] or (i>0 and nums[i] == nums[i-1] and (not used[i-1])):
                    continue

                used[i] = True
                tmp.append(nums[i])
                backtrack(nums, i + 1, res, tmp,used)
                tmp.pop()
                used[i] = False

        res = []
        nums.sort()
        used = [False for _ in range(0,len(nums))]
        backtrack(nums, 0, res, [], used)
        return res

Solution_sample = Solution()
# nums  = [1,1,2]
# nums = [1,1]

nums = [3,3,0,3]
# 期望结果:[[0,3,3,3],[3,0,3,3],[3,3,0,3],[3,3,3,0]]
res = Solution_sample.permuteUnique(nums)
print(res)