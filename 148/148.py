# 给你链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表 。
#
#
#
#
#
#
#  示例 1：
#
#
# 输入：head = [4,2,1,3]
# 输出：[1,2,3,4]
#
#
#  示例 2：
#
#
# 输入：head = [-1,5,3,4,0]
# 输出：[-1,0,3,4,5]
#
#
#  示例 3：
#
#
# 输入：head = []
# 输出：[]
#
#
#
#
#  提示：
#
#
#  链表中节点的数目在范围 [0, 5 * 10⁴] 内
#  -10⁵ <= Node.val <= 10⁵
#
#
#
#
#  进阶：你可以在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序吗？
#
#  Related Topics 链表 双指针 分治 排序 归并排序 👍 2308 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def hepler(left,right):
            dummy_head = ListNode(0)
            cur = dummy_head
            while(left and right):
                if left.val < right.val:
                    cur.next = left
                    left = left.next
                else:
                    cur.next = right
                    right = right.next
                cur = cur.next

            if(left):
               cur.next = left
            if(right):
                cur.next = right

            return dummy_head.next

        def merge_sort(node):
            if not node or not node.next:
                return node
            slow = node
            fast = node.next
            while(fast and fast.next):
                fast = fast.next.next
                slow = slow.next

            left = node
            right = slow.next

            slow.next =None
            return hepler(merge_sort(left)  ,merge_sort(right))

        return merge_sort(head)