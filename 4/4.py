# 给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。
#
#  算法的时间复杂度应该为 O(log (m+n)) 。
#
#
#
#  示例 1：
#
#
# 输入：nums1 = [1,3], nums2 = [2]
# 输出：2.00000
# 解释：合并数组 = [1,2,3] ，中位数 2
#
#
#  示例 2：
#
#
# 输入：nums1 = [1,2], nums2 = [3,4]
# 输出：2.50000
# 解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5
#
#
#
#
#
#
#  提示：
#
#
#  nums1.length == m
#  nums2.length == n
#  0 <= m <= 1000
#  0 <= n <= 1000
#  1 <= m + n <= 2000
#  -10⁶ <= nums1[i], nums2[i] <= 10⁶
#
#
#  Related Topics 数组 二分查找 分治 👍 6844 👎 0
from typing import List

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 求得数组nums1的元素个数
        len_nums1 = len(nums1)
        # 求得数组nums2的元素个数
        len_nums2 = len(nums2)
        # 相加求得元素总数
        len_sum = len_nums1 + len_nums2

        # 要对len_sum为奇数以及偶数的情况都做相应的适配
        median_left = (len_sum + 1) // 2
        # 此处为什么是(len_sum+1//2)以及(len_sum+2)//2?
        # 考虑到数组中元素的下标从0开始计数，而此处我们求得是将两个数组合并后从1开始的第k个数（或者第k和第k+1个数的平均值）作为最终结果的。这里的k之所以为从1开始数的，是因为在之后要排除掉前a个元素（假设前a个元素都小于两个数组合并后的中位数），这样直接计算k-a即可。
        median_right = (len_sum + 2) // 2
        # 返回结果为两个数组递归得到中位数即第k个值（奇数的情况），或者第k和k+1个值得平均数（偶数的情况）
        return (Solution.getKth(self, nums1, 0, len_nums1 - 1, nums2, 0, len_nums2 - 1, median_left) + Solution.getKth(
            self, nums1, 0, len_nums1 - 1, nums2, 0, len_nums2 - 1, median_right)) * 0.5

    def getKth(self, nums1: List[int], start_1: int, end_1: int, nums2: List[int], start_2: int, end_2: int, k: int):
        len_1 = end_1 - start_1 + 1
        len_2 = end_2 - start_2 + 1
        # 若nums1的元素个数大于nums2，此时调换两个数组，方便进行统一处理
        if len_1 > len_2:
            return Solution.getKth(self, nums2, start_2, end_2, nums1, start_1, end_1, k)
        # 若nums1数组（由于上一步做过处理，nums1肯定是元素较少的那个数组）为空，则只需要直接返回数组而的中位数。此处无需考虑偶数的情况，因为在findMedianSortedArrays里已经考虑过了。
        if len_1 == 0:
            return nums2[start_2 + k - 1]
        # 若k等于1的时候，此时说明计算范围内的数组元素中，第一个就是要求的结果（数组中下标为0），则直接取得两个数组首个元素中较小的那一个即可。同样奇偶性不需要考虑，在findMediaSortedArrays里已经考虑过了。
        if k == 1:
            return min(nums1[start_1], nums2[start_2])

        # 此处理解花费时间较长：由于之前我们定义的k是从1开始数的第k个元素，此处要在数组中找到对应的元素，下标应该-1。同样因为len计算的是元素的总数，会比数组最后一个元素的下标大1，所以不论取哪个值，都需要减去1。
        pointer_1 = start_1 + min(len_1, k // 2) - 1
        pointer_2 = start_2 + min(len_2, k // 2) - 1
        # 判断两个指针指向的元素值得大小，去掉较小元素所在数组的在较小元素之前的元素以及较小元素，将指针指向较小元素的后一个值。之后进行递归处理即可得到结果。
        if nums1[pointer_1] > nums2[pointer_2]:
            return Solution.getKth(self, nums1, start_1, end_1, nums2, pointer_2 + 1, end_2,
                                   k - (pointer_2 - start_2 + 1))
        else:
            return Solution.getKth(self, nums1, pointer_1 + 1, end_1, nums2, start_2, end_2,
                                   k - (pointer_1 - start_1 + 1))


Solution_sample = Solution()
# nums1 = [1,2]
# nums2 = [3,4]
# 中位数 (2 + 3) / 2 = 2.5


# nums1 = [1]
# nums2 = [2,3,4]

nums1 =[1,3]
nums2 = [2]
# 期望结果:2.00000
res = Solution_sample.findMedianSortedArrays(nums1,nums2)
print(res)