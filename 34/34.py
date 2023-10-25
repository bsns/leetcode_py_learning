# 给你一个按照非递减顺序排列的整数数组 nums，和一个目标值 target。请你找出给定目标值在数组中的开始位置和结束位置。
#
#  如果数组中不存在目标值 target，返回 [-1, -1]。
#
#  你必须设计并实现时间复杂度为 O(log n) 的算法解决此问题。
#
#
#
#  示例 1：
#
#
# 输入：nums = [5,7,7,8,8,10], target = 8
# 输出：[3,4]
#
#  示例 2：
#
#
# 输入：nums = [5,7,7,8,8,10], target = 6
# 输出：[-1,-1]
#
#  示例 3：
#
#
# 输入：nums = [], target = 0
# 输出：[-1,-1]
#
#
#
#  提示：
#
#
#  0 <= nums.length <= 10⁵
#  -10⁹ <= nums[i] <= 10⁹
#  nums 是一个非递减数组
#  -10⁹ <= target <= 10⁹
#
#
#  Related Topics 数组 二分查找 👍 2517 👎 0

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # 输入：nums = [5, 7, 7, 8, 8, 10], target = 8
        # 输出：[3, 4]
        #
        n = len(nums)
        left,right = 0,n-1

        left_idx = float('inf')
        while(left<=right):
            mid = (right-left)//2 + left

            if nums[mid] == target:
                left_idx = min(left_idx,mid)
                right=mid-1
            elif(nums[mid] < target):
                left=mid+1
            else:
                right = mid - 1



        right_idx = -float('inf')
        left, right = 0, n - 1
        while (left <= right):
            mid = (right - left) // 2 + left

            if nums[mid] == target:
                right_idx = max(right_idx, mid)
                left = mid + 1
            elif (nums[mid] < target):
                left = mid + 1
            else:
                right = mid - 1

        if right_idx>=0:
            return [left_idx,right_idx]
        else:
            return[-1,-1]

Solution_sample = Solution()

# nums = [5, 7, 7, 8, 8, 10]
# target = 8
# 输出：[3, 4]


nums = [1]
target = 1
# 测试用例:[1]
#
# 测试结果:[-1,-1]
# 期望结果:[0,0]
res = Solution_sample.searchRange(nums,target)
print(res)