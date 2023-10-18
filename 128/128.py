# 给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。
#
#  请你设计并实现时间复杂度为 O(n) 的算法解决此问题。
#
#
#
#  示例 1：
#
#
# 输入：nums = [100,4,200,1,3,2]
# 输出：4
# 解释：最长数字连续序列是 [1, 2, 3, 4]。它的长度为 4。
#
#  示例 2：
#
#
# 输入：nums = [0,3,7,2,5,8,4,6,0,1]
# 输出：9
#
#
#
#
#  提示：
#
#
#  0 <= nums.length <= 10⁵
#  -10⁹ <= nums[i] <= 10⁹
#
#
#  Related Topics 并查集 数组 哈希表 👍 1855 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestConsecutive(self, nums):

        recorder = {}
        max_length = 0
        for i in range(0,len(nums)):

            if nums[i] not in recorder:
                left = recorder.get(nums[i]-1,0)
                right = recorder.get(nums[i]+1,0)
                cur_length = left+right+1
                if cur_length>max_length:
                    max_length = cur_length

                recorder[nums[i]] = cur_length
                recorder[nums[i]-left] = cur_length
                recorder[nums[i]+right] = cur_length

        return max_length

Solution_sample = Solution()

# nums = [100,4,200,1,3,2]
nums  = [0,3,7,2,5,8,4,6,0,1]
res = Solution_sample.longestConsecutive(nums)

print(res)
