# 给定一个已排序的链表的头
#  head ， 删除所有重复的元素，使每个元素只出现一次 。返回 已排序的链表 。
#
#
#
#  示例 1：
#
#
# 输入：head = [1,1,2]
# 输出：[1,2]
#
#
#  示例 2：
#
#
# 输入：head = [1,1,2,3,3]
# 输出：[1,2,3]
#
#
#
#
#  提示：
#
#
#  链表中节点数目在范围 [0, 300] 内
#  -100 <= Node.val <= 100
#  题目数据保证链表已经按升序 排列
#
#
#  Related Topics 链表 👍 1125 👎 0

from typing import Optional
# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # head = [1, 1, 2, 3, 3]
        if not head:
            return head
        dummy_head = ListNode(0)
        dummy_head.next = head
        slow = head
        fast = slow.next
        # pre = dummy_head
        while (fast):
            if fast.val != slow.val:
                slow.next = fast
                slow = slow.next
            fast = fast.next
        slow.next = None
        return dummy_head.next


Solution_demo = Solution()
root = ListNode(1)
root.next = ListNode(1)
root.next.next = ListNode(2)
root.next.next.next = ListNode(3)
root.next.next.next.next = ListNode(3)
# 测试用例:[1,1,2,3,3]
# 	测试结果:[1,2,3,3]
# 	期望结果:[1,2,3]
res = Solution_demo.deleteDuplicates(root)

while(res):
    print(res.val)
    res = res.next
