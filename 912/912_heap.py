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
        def heapify(arr,n,i):
            if i>=n:
                return
            largest = i
            lchild = 2*i+1
            rchild = 2*i+2

            if lchild<n and arr[largest] < arr[lchild]:
                largest = lchild
            if rchild<n and arr[largest] < arr[rchild]:
                largest = rchild
            if largest!=i :
                arr[i],arr[largest] = arr[largest],arr[i]
                heapify(nums,n,largest)

        n = len(nums)
        for i in range(n,-1,-1):
            heapify(nums,n,i)

        for i in range(n-1,-1,-1):
            nums[0],nums[i] = nums[i],nums[0]
            heapify(nums,i,0)
        return nums
        # def heapify(arr, n, i):
        #     # 递归条件出口
        #     if i >= n:
        #         return
        #         # 默认i为最大
        #     largest = i
        #     lchild = 2 * i + 1
        #     rchild = 2 * i + 2
        #     if lchild < n and arr[largest] < arr[lchild]:
        #         largest = lchild
        #     if rchild < n and arr[largest] < arr[rchild]:
        #         largest = rchild
        #     if largest != i:
        #         arr[i], arr[largest] = arr[largest], arr[i]
        #         # 递归，从节点开始
        #         heapify(arr, n, largest)
        #
        # n = len(nums)
        # # 从后向前直到index为0
        # for i in range(n, -1, -1):
        #     # n是长度不会变，i是从最后一个节点一直到index为0
        #     heapify(nums, n, i)
        #     # 这个为什么是n-1，是因为这个n-1代表最后一个堆的index
        # for i in range(n - 1, 0, -1):
        #     nums[0], nums[i], = nums[i], nums[0]
        #     # 这里为什么是i在这里，是因为长度是随着每次交换最后1个，长度就减1，一直到0
        #     heapify(nums, i, 0)
        # return nums


Solution_sample = Solution()
nums = [5,1,1,2,0,0]
res = Solution_sample.sortArray(nums)
print(res)