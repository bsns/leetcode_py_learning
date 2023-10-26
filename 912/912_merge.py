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
        def merge(left,right):
            res = []
            i=0
            j=0
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    res.append(left[i])
                    i+=1
                else:
                    res.append(right[j])
                    j+=1
            res+=left[i:]
            res+=right[j:]
            return res

        if len(nums) <= 1:
            return nums
        mid = len(nums) //2
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])

        return merge(left,right)



Solution_sample = Solution()
nums = [5,1,1,2,0,0]
res = Solution_sample.sortArray(nums)
print(res)