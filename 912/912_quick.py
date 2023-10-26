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
        def quick(nums,start,end):
            if start>= end:
                return

            left,right = start,end
            pivot = left
            while(left < right):
                while(left < right and nums[right]> nums[pivot]):
                    right-=1
                while(left<right and nums[left] <=nums[pivot]):
                    left +=1
                nums[left],nums[right] = nums[right],nums[left]
            nums[pivot], nums[right] = nums[right], nums[pivot]
            quick(nums,start,right-1)
            quick(nums,right+1,end)
        quick(nums,0,n-1)

        return nums


Solution_sample = Solution()
nums = [5,1,1,2,0,0]
res = Solution_sample.sortArray(nums)
print(res)