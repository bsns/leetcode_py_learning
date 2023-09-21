# 给定一个单链表 L 的头节点 head ，单链表 L 表示为：
#
#
# L0 → L1 → … → Ln - 1 → Ln
#
#
#  请将其重新排列后变为：
#
#
# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
#
#  不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
#
#
#
#  示例 1：
#
#
#
#
# 输入：head = [1,2,3,4]
# 输出：[1,4,2,3]
#
#  示例 2：
#
#
#
#
# 输入：head = [1,2,3,4,5]
# 输出：[1,5,2,4,3]
#
#
#
#  提示：
#
#
#  链表的长度范围为 [1, 5 * 10⁴]
#  1 <= node.val <= 1000
#
#
#  Related Topics 栈 递归 链表 双指针 👍 1371 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        fast = slow = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next



        # 456
        # dummy_part 4
        # dummy_part.next
        # 654
        cur = slow.next
        slow.next = None

        dummy_head = ListNode(0)
        while(cur):
            dummy_head_next = dummy_head.next
            dummy_head.next = cur
            cur = cur.next
            dummy_head.next.next = dummy_head_next

        first = head
        second = dummy_head.next
        dummy_res = ListNode(0)

        cur = dummy_res
        while(first or second):
            if(first):
                cur.next = first
                first = first.next
                cur = cur.next
            if(second):
                cur.next =second
                second = second.next
                cur = cur.next
        return dummy_res.next



a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
# 测试用例:[1,2,3,4]
# 	测试结果:[1,2,3]
# 	期望结果:[1,4,2,3]

a.next = b
b.next = c
c.next = d

Solution_sample = Solution()
res = Solution_sample.reorderList(head=a)

while(res):
    print(res.val)
    res = res.next