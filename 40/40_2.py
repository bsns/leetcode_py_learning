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
        def dfs(begin, path, residue):
            if residue == 0:
                res.append(path[:])
                return

            for index in range(begin, size):
                if candidates[index] > residue:
                    break

                if index > begin and candidates[index - 1] == candidates[index]:
                    continue

                path.append(candidates[index])
                dfs(index + 1, path, residue - candidates[index])
                path.pop()

        size = len(candidates)
        if size == 0:
            return []

        candidates.sort()
        res = []
        dfs(0, [], target)
        return res


Solution_sample = Solution()
candidates =[10,1,2,7,6,1,5]
target =8
res = Solution_sample.combinationSum2(candidates,target)
print(res)