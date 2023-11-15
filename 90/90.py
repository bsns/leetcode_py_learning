# 给你一个整数数组 nums ，其中可能包含重复元素，请你返回该数组所有可能的子集（幂集）。
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
#  Related Topics 位运算 数组 回溯 👍 1170 👎 0

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        def dfs(i,path,res,used):
            if i>len(nums) : # or len(path) > len(nums):
                return

            res.append(path[:])

            # path.append(nums[i])

            for j in range(i,len(nums)):
                if used[j] == True:
                    continue

                if j>i and nums[j] == nums[j-1] and used[j-1] == False:
                    continue
                used[j] = True
                dfs(j,path+ [nums[j]],res,used)
                used[j]=False
            # path.pop()
        path = []
        res = []

        nums.sort()
        used = [False for _ in  range(len(nums))]
        dfs(0,path,res,used)

        return res

Solution_sample = Solution()

# nums = [1,2,2]

nums = [4,4,4,1,4]
# 测试用例:[4,4,4,1,4]
# 	测试结果:[[],[4],[4,4],[4,4,4],[4,4,4,1],[4,4,4,1,4],[4,4,4,4],[4,4,1],[4,4,1,4],[4,4,4],[4,1],[4,1,4],[4,4],[1],[1,4],[4]]
# 	期望结果:[[],[1],[1,4],[1,4,4],[1,4,4,4],[1,4,4,4,4],[4],[4,4],[4,4,4],[4,4,4,4]]
res = Solution_sample.subsetsWithDup(nums)
print(res)