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
#  Related Topics 数组 回溯 👍 1494 👎 0

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        def dfs(path,res,i,used):
            # if i > len(nums):
            #     return

            if len(path) == len(nums):
                res.append(path[:])

                # return

            for j in range(0,len(nums)):
                if j > 0 and nums[j] == nums[j - 1] and used[j-1] ==True:
                    continue
                if used[j] == True:
                    continue
                # if j> len(nums)-1:
                #     break
                used[j] = True
                dfs(path+[nums[j]],res,j+1,used)
                used[j] =False
            #     path.pop()




        path = []
        res = []
        i = 0
        used = [False for _ in range(len(nums))]
        nums.sort()
        dfs(path,res,0,used)

        return res


Solution_sample = Solution()
# nums = [1,2,3]
nums = [1,1,2]
res = Solution_sample.permuteUnique(nums)
print(res)