# 给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。
#
#  请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
#
#  你必须设计并实现时间复杂度为 O(n) 的算法解决此问题。
#
#
#
#  示例 1:
#
#
# 输入: [3,2,1,5,6,4], k = 2
# 输出: 5
#
#
#  示例 2:
#
#
# 输入: [3,2,3,1,2,4,5,5,6], k = 4
# 输出: 4
#
#
#
#  提示：
#
#
#  1 <= k <= nums.length <= 10⁵
#  -10⁴ <= nums[i] <= 10⁴
#
#
#  Related Topics 数组 分治 快速选择 排序 堆（优先队列） 👍 2327 👎 0

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quickSelect(nums, left, right, k):
            pivot_index = partition(nums, left, right)
            # If pivot_index is equal to k, we found the k-th largest element
            if pivot_index == k:
                return nums[pivot_index]
            elif pivot_index < k:
                # Search in the right part
                return quickSelect(nums, pivot_index + 1, right, k)
            else:
                # Search in the left part
                return quickSelect(nums, left, pivot_index - 1, k)

        def partition(nums, left, right):
            pivot = nums[right]
            p_index = left
            for i in range(left, right):
                if nums[i] >= pivot:  # Change comparison to >= for finding kth largest
                    nums[i], nums[p_index] = nums[p_index], nums[i]
                    p_index += 1
            nums[p_index], nums[right] = nums[right], nums[p_index]
            return p_index

        # We are looking for the k-th largest, which is the (len(nums) - k) smallest in 0-based index
        return quickSelect(nums, 0, len(nums) - 1, k - 1)


Solution_demo = Solution()
nums = [3,2,1,5,6,4]
k = 2
res = Solution_demo.findKthLargest(nums,k)
print(res)