# 给定一组非负整数 nums，重新排列每个数的顺序（每个数不可拆分）使之组成一个最大的整数。
#
#  注意：输出结果可能非常大，所以你需要返回一个字符串而不是整数。
#
#
#
#  示例 1：
#
#
# 输入：nums = [10,2]
# 输出："210"
#
#  示例 2：
#
#
# 输入：nums = [3,30,34,5,9]
# 输出："9534330"
#
#
#
#
#  提示：
#
#
#  1 <= nums.length <= 100
#  0 <= nums[i] <= 10⁹
#
#
#  Related Topics 贪心 数组 字符串 排序 👍 1210 👎 0

from typing import  List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
# leetcode submit region end(Prohibit modification and deletion)
#         输入：nums = [3, 30, 34, 5, 9]
#         输出："9534330"
#         提示：
#           [333,333,334]

          nums = list(map(str,nums))
          compare = lambda x,y :1 if x+y < y+x else -1
          import functools
          nums =sorted(nums, key=functools.cmp_to_key(compare))
          # nums.reverse()
          res = "".join(nums)
          if(res[0] == "0"):
              res = "0"
          return res



Solution_sample = Solution()
# 输入：nums = [3,30,34,5,9] 输出："9534330"
# nums = [3,30,34,5,9]


nums = [3,30,34,5,9]

# 测试用例:[3,30,34,5,9]
# 	测试结果:"9534303"
# 	期望结果:"9534330"
res = Solution_sample.largestNumber(nums)
print(res)