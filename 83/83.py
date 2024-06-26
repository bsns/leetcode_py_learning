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
#  Related Topics 链表 👍 1120 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

            if not head:
                return head
            slow = head
            fast = head.next

            while(fast):

                if(slow.val != fast.val):
                    slow = slow.next
                    slow.val = fast.val

                fast = fast.next
            slow.next =None

            return head
