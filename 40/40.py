# 给定一个候选人编号的集合 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
#
#  candidates 中的每个数字在每个组合中只能使用 一次 。
#
#  注意：解集不能包含重复的组合。
#
#
#
#  示例 1:
#
#
# 输入: candidates = [10,1,2,7,6,1,5], target = 8,
# 输出:
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ]
#
#  示例 2:
#
#
# 输入: candidates = [2,5,2,1,2], target = 5,
# 输出:
# [
# [1,2,2],
# [5]
# ]
#
#
#
#  提示:
#
#
#  1 <= candidates.length <= 100
#  1 <= candidates[i] <= 50
#  1 <= target <= 30
#
#
#  Related Topics 数组 回溯 👍 1476 👎 0

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(path,res,need,i,used):


            if need == 0:
                res.append(path[:])

            # path.append(candidates[i])
            for j in range(i,len(candidates)):
                if (j> len(candidates)) or candidates[j]> need:
                    break
                # print(j)
                if j>i and candidates[j] == candidates[j-1]:
                    continue
                if used[j] == True:
                    continue
                used[j] = True
                dfs(path+[candidates[j]],res,need-candidates[j],j+1,used)
                used[j] =False
            # path.pop()

        path = []
        res = []
        used = [False  for _ in range(len(candidates))]
        candidates.sort()
        dfs(path,res,target,0,used)
        return res


Solution_sample = Solution()
candidates =[10,1,2,7,6,1,5]
target =8
# 期望结果:[[1,1,6],[1,2,5],[1,7],[2,6]]

res = Solution_sample.combinationSum2(candidates,target)
print(res)