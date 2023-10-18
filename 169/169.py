# 给定一个大小为 n 的数组 nums ，返回其中的多数元素。多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。
#
#  你可以假设数组是非空的，并且给定的数组总是存在多数元素。
#
#
#
#  示例 1：
#
#
# 输入：nums = [3,2,3]
# 输出：3
#
#  示例 2：
#
#
# 输入：nums = [2,2,1,1,1,2,2]
# 输出：2
#
#
#
# 提示：
#
#
#  n == nums.length'
#  1 <= n <= 5 * 10⁴
#  -10⁹ <= nums[i] <= 10⁹
#
#
#
#
#  进阶：尝试设计时间复杂度为 O(n)、空间复杂度为 O(1) 的算法解决此问题。
#
#  Related Topics 数组 哈希表 分治 计数 排序 👍 2005 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def majorityElement(self, nums):
        record = {}
        n = len(nums)
        for i in range(0, n):
            if nums[i] in record:
                record[nums[i]] += 1
            else:
                record[nums[i]] = 1
            if record[nums[i]] > n / 2:
                return nums[i]
        return None

