# 给你一个整数数组 nums，请你将该数组升序排列。
#
#
#
#
#
#
#  示例 1：
#
#
# 输入：nums = [5,2,3,1]
# 输出：[1,2,3,5]
#
#
#  示例 2：
#
#
# 输入：nums = [5,1,1,2,0,0]
# 输出：[0,0,1,1,2,5]
#
#
#
#
#  提示：
#
#
#  1 <= nums.length <= 5 * 10⁴
#  -5 * 10⁴ <= nums[i] <= 5 * 10⁴
#
#
#  Related Topics 数组 分治 桶排序 计数排序 基数排序 排序 堆（优先队列） 归并排序 👍 928 👎 0
from typing import List

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for c in range(n):
            for i in range(1,n-c):
                if(nums[i-1]>nums[i]):
                    nums[i-1],nums[i] = nums[i],nums[i-1]
        return nums


Solution_sample = Solution()
nums = [5,1,1,2,0,0]
res = Solution_sample.sortArray(nums)
print(res)