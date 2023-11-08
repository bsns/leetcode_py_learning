# 给你一个整数数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位
# 。
#
#  返回 滑动窗口中的最大值 。
#
#
#
#  示例 1：
#
#
# 输入：nums = [1,3,-1,-3,5,3,6,7], k = 3
# 输出：[3,3,5,5,6,7]
# 解释：
# 滑动窗口的位置                最大值
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7
#
#
#  示例 2：
#
#
# 输入：nums = [1], k = 1
# 输出：[1]
#
#
#
#
#  提示：
#
#
#  1 <= nums.length <= 10⁵
#  -10⁴ <= nums[i] <= 10⁴
#  1 <= k <= nums.length
#
#
#  Related Topics 队列 数组 滑动窗口 单调队列 堆（优先队列） 👍 2592 👎 0

from typing import List
import collections
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        deque = collections.deque()
        n = len(nums)
        res = []
        for i,j in zip(range(1-k,n+1-k),range(n)):
            if i>0 and deque[0] == nums[i-1]:
                deque.popleft()
            while deque and deque[-1] < nums[j]:
                deque.pop()
            deque.append(nums[j])
            if i>=0:
                res.append(deque[0])
        return res


Solution_sample = Solution()
# 输入：nums = [1,3,-1,-3,5,3,6,7], k = 3 输出：[3,3,5,5,6,7]
nums = [1,3,-1,-3,5,3,6,7]
k = 3
res = Solution_sample.maxSlidingWindow(nums,k)
print(res)