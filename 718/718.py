# 给两个整数数组 nums1 和 nums2 ，返回 两个数组中 公共的 、长度最长的子数组的长度 。
#
#
#
#  示例 1：
#
#
# 输入：nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]
# 输出：3
# 解释：长度最长的公共子数组是 [3,2,1] 。
#
#
#  示例 2：
#
#
# 输入：nums1 = [0,0,0,0,0], nums2 = [0,0,0,0,0]
# 输出：5
#
#
#
#
#  提示：
#
#
#  1 <= nums1.length, nums2.length <= 1000
#  0 <= nums1[i], nums2[i] <= 100
#
#
#  Related Topics 数组 二分查找 动态规划 滑动窗口 哈希函数 滚动哈希 👍 1016 👎 0

from typing import  List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:

        m = len(nums1) + 1
        n = len(nums2) + 1

        dp = [[0 for _ in range(n)] for _ in range(m)]
        res = 0
        for i in range(1, m):
            for j in range(1, n):
                # print(i-1,j-1)

                if nums1[i - 1] == nums2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                # else:
                #     dp[i][j] = 0#dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                    res = max(res,dp[i][j])
        return res#dp[m - 1][n - 1]

Solution_sample = Solution()
nums1 = [1,2,3,2,1]
nums2 = [3,2,1,4,7]

res = Solution_sample.findLength(nums1,nums2)
print(res)