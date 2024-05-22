# 给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。
#
#
#
#  示例 1：
#
#
# 输入：head = [1,2,3,4,5], n = 2
# 输出：[1,2,3,5]
#
#
#  示例 2：
#
#
# 输入：head = [1], n = 1
# 输出：[]
#
#
#  示例 3：
#
#
# 输入：head = [1,2], n = 1
# 输出：[1]
#
#
#
#
#  提示：
#
#
#  链表中结点的数目为 sz
#  1 <= sz <= 30
#  0 <= Node.val <= 100
#  1 <= n <= sz
#
#
#
#
#  进阶：你能尝试使用一趟扫描实现吗？
#
#  Related Topics 链表 双指针 👍 2854 👎 0

from typing import Optional
# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        def find(head,k):
            fast = head
            slow = head
            for i in range(k):
                fast = fast.next

            while(fast):
                fast = fast.next
                slow = slow.next

            return slow

        dummy_head = ListNode(0)
        dummy_head.next = head
        node_n_1 = find(dummy_head,n+1)

        right = node_n_1.next.next
        node_n_1.next = right

        return dummy_head.next


# head = [1,2,3,4,5], n = 2

# head = ListNode(1)
# head.next = ListNode(2)
# head.next.next = ListNode(3)
# head.next.next.next = ListNode(4)
# head.next.next.next.next = ListNode(5)
# n = 2



head = ListNode(1)

n = 1
Solution_Demo = Solution()

res = Solution_Demo.removeNthFromEnd(head,n)

while(res):
    print(res.val)
    res=res.next