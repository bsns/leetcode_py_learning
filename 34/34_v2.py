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
#  Related Topics 数组 二分查找 👍 2672 👎 0

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def left_bound(nums,target):
            left,right = 0,len(nums)-1
            while(left <= right):
                mid = (left+right)//2
                if nums[mid] == target:
                    right = mid-1
                elif(nums[mid]<target):
                    left = mid +1
                elif(nums[mid]>target):
                    right = mid-1
            if left < 0 or left>=len(nums):
                return -1
            return left if nums[left]== target else -1

        def right_bound(nums,target):
            left,right = 0,len(nums)-1
            while(left <= right):
                mid = (left+right)//2
                if nums[mid] == target:
                    left = mid+1
                elif(nums[mid]<target):
                    left = mid +1
                elif(nums[mid]>target):
                    right = mid-1
            if right < 0 or right>=len(nums):
                return -1
            return right if nums[right]== target else -1




        left = left_bound(nums,target)
        right  = right_bound(nums,target)

        return [left,right]


Solution_demo = Solution()
# nums =[5,7,7,7,8,10]
# target = 8
# 输入：nums = [5,7,7,8,8,10], target = 8
# 输出：[3,4]
nums = [5,7,7,8,8,10]
target = 8
# nums = [1]
# target = 1
# 期望结果:[0,0]
res = Solution_demo.searchRange(nums,target)
print(res)