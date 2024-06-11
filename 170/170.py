# 在股票交易中，如果前一天的股价高于后一天的股价，则可以认为存在一个「交易逆序对」。请设计一个程序，输入一段时间内的股票交易记录 record，返回其中存在的
# 「交易逆序对」总数。
#
#
#
#  示例 1:
#
#
# 输入：record = [9, 7, 5, 4, 6]
# 输出：8
# 解释：交易中的逆序对为 (9, 7), (9, 5), (9, 4), (9, 6), (7, 5), (7, 4), (7, 6), (5, 4)。
#
#
#
#
#  限制：
#
#  0 <= record.length <= 50000
#
#  Related Topics 树状数组 线段树 数组 二分查找 分治 有序集合 归并排序 👍 1103 👎 0

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def reversePairs(self, record: List[int]) -> int:

        def merge_sort(arr):
            """归并排序"""
            if len(arr) == 1:
                return arr
            # 使用二分法将数列分两个
            mid = len(arr) // 2
            left = arr[:mid]
            right = arr[mid:]
            # 使用递归运算
            return marge(merge_sort(left), merge_sort(right))

        def marge(left, right):
            """排序合并两个数列"""
            result = []
            # 两个数列都有值
            while len(left) > 0 and len(right) > 0:
                # 左右两个数列第一个最小放前面
                if left[0] <= right[0]:
                    result.append(left.pop(0))
                else:
                    self.res+=len(left)
                    result.append(right.pop(0))
            # 只有一个数列中还有值，直接添加
            result += left
            result += right
            return result
        self.res = 0
        merge_sort(record)
        return self.res



Solution_demo = Solution()
# record = [9, 7, 5, 4, 6]


record = [1,3,2,3,1]
# 测试用例:[1,3,2,3,1]
# 	测试结果:8
# 	期望结果:4
res = Solution_demo.reversePairs(record)
print(res)

