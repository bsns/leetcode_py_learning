# 给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j !=
# k ，同时还满足 nums[i] + nums[j] + nums[k] == 0 。请
#
#  你返回所有和为 0 且不重复的三元组。
#
#  注意：答案中不可以包含重复的三元组。
#
#
#
#
#
#  示例 1：
#
#
# 输入：nums = [-1,0,1,2,-1,-4]
# 输出：[[-1,-1,2],[-1,0,1]]
# 解释：
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0 。
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0 。
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0 。
# 不同的三元组是 [-1,0,1] 和 [-1,-1,2] 。
# 注意，输出的顺序和三元组的顺序并不重要。
#
#
#  示例 2：
#
#
# 输入：nums = [0,1,1]
# 输出：[]
# 解释：唯一可能的三元组和不为 0 。
#
#
#  示例 3：
#
#
# 输入：nums = [0,0,0]
# 输出：[[0,0,0]]
# 解释：唯一可能的三元组和为 0 。
#
#
#
#
#  提示：
#
#
#  3 <= nums.length <= 3000
#  -10⁵ <= nums[i] <= 10⁵
#
#
#  Related Topics 数组 双指针 排序 👍 6432 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def threeSum(self, nums):

        nums.sort()
        res = []
        n = len(nums)
        # [-4, -1, -1, 0, 1, 2]
        for i in range(0,n-2):
            j = i + 1
            k = n-1

            if nums[i] > 0:
                break

            if i >0 and nums[i] == nums[i - 1]:
                continue

            while(j<k):
                tmp_sum = nums[i] + nums[j] + nums[k]
                if (tmp_sum<0):
                    j+=1
                elif(tmp_sum>0):
                    k-=1

                else:
                    res.append([nums[i],nums[j],nums[k]])
                    j = j + 1
                    k = k - 1
                    while(nums[j-1] ==nums[j] and j<k):
                        j+=1
                    while(nums[k+1] == nums[k] and j<k):
                        k-=1


        return res


Solution_sample = Solution()
# nums = [-1,0,1,2,-1,-4]

nums = [0,0,0]
# 期望结果:[[0,0,0]]
res = Solution_sample.threeSum(nums)
print(res)