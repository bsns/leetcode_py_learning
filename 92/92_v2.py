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
from typing import  Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        dummy_head = ListNode(0)
        dummy_head.next = head

        pre = dummy_head
        cur = head
        for i in range(left-1):
            cur = cur.next
            pre = pre.next

        # 1 2 3   4  5  6  7 8
        #     pre cur
        new_rev_head = None
        mark_mid = cur
        for i in range(left-1, right):
            cur_next = cur.next
            cur.next = new_rev_head

            pre.next = cur
            new_rev_head = cur
            cur = cur_next

        mark_mid.next = cur
        return dummy_head.next


def buildList(nums):
    head = None
    tail = None

    for num in nums:
        if not head:
            head = tail = ListNode(num)
        else:
            tail.next = ListNode(num)
            tail = tail.next

    return head


def printList(head):
    while head:
        print(head.val, end=" ")
        head = head.next
    print()


if __name__ == "__main__":
    data = [
        ([1, 2, 3, 4, 5], 2, 4, [1, 4, 3, 2, 5]),
        # ([3,5], 1, 2, [5,3]),
        # ([1, 2, 3], 1, 2, [2, 1, 3]),
        # ([1, 2, 3], 2, 3, [1, 3, 2]),
        # ([1, 2, 3, 4, 5], 1, 4, [4, 1, 2, 3, 5]),
    ]

    Solution_demo = Solution()
    for nums, left, right, expected in data:
        head = buildList(nums)
        printList(head)
        head = Solution_demo.reverseBetween(head, left, right)
        printList(head)