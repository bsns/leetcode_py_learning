# 给你单链表的头指针 head 和两个整数 left 和 right ，其中 left <= right 。请你反转从位置 left 到位置 right 的链
# 表节点，返回 反转后的链表 。
#
#
#
#  示例 1：
#
#
# 输入：head = [1,2,3,4,5], left = 2, right = 4
# 输出：[1,4,3,2,5]
#
#
#  示例 2：
#
#
# 输入：head = [5], left = 1, right = 1
# 输出：[5]
#
#
#
#
#  提示：
#
#
#  链表中节点数目为 n
#  1 <= n <= 500
#  -500 <= Node.val <= 500
#  1 <= left <= right <= n
#
#
#
#
#  进阶： 你可以使用一趟扫描完成反转吗？
#
#  Related Topics 链表 👍 1651 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        # 输入：head = [1,2,3,4,5], left = 2, right = 4
        # 输出：[1,4,3,2,5]
        # 012345
        # 012345
        #  l  r
        # 01 23 45
        if (left == right):
            return head
        dummy_head = ListNode(0)
        dummy_head.next = head
        times = right - left + 1

        l, r = dummy_head, dummy_head
        while (right > 0):
            r = r.next
            right -= 1
            left -= 1
            if (left > 0):
                # left -=1
                l = l.next
        mid_head = l.next
        right_left = r.next

        # 23 4

        # 1 2
        #  l l.next
        #    mid mid.next
        #   #3 4
        # l_origin_next = l.next
        # l.next = mid
        # mid = mid.next
        # l.next.next = l_origin_next

        # 1 3 2
        # 1 4 3 2
        # times = right - left
        mid_origin = l.next
        while (times):
            l_origin_next = l.next
            l.next = mid_head
            mid_head = mid_head.next
            l.next.next = l_origin_next
            # l = l.next
            times -= 1
        mid_origin.next = right_left

        return dummy_head.next