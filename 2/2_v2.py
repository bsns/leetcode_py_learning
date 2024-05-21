# 给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。
#
#  请你将两个数相加，并以相同形式返回一个表示和的链表。
#
#  你可以假设除了数字 0 之外，这两个数都不会以 0 开头。
#
#
#
#  示例 1：
#
#
# 输入：l1 = [2,4,3], l2 = [5,6,4]
# 输出：[7,0,8]
# 解释：342 + 465 = 807.
#
#
#  示例 2：
#
#
# 输入：l1 = [0], l2 = [0]
# 输出：[0]
#
#
#  示例 3：
#
#
# 输入：l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# 输出：[8,9,9,9,0,0,0,1]
#
#
#
#
#  提示：
#
#
#  每个链表中的节点数在范围 [1, 100] 内
#  0 <= Node.val <= 9
#  题目数据保证列表表示的数字不含前导零
#
#
#  Related Topics 递归 链表 数学 👍 10333 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(0)
        link = dummy_head
        flag = 0
        while (l1 and l2):
            cur_val = flag + l1.val + l2.val
            l1 = l1.next
            l2 = l2.next
            if cur_val >= 10:
                flag = 1
                cur_val = cur_val - 10
            else:
                flag = 0
            cur = ListNode(cur_val)
            link.next = cur
            link = link.next

        while (l1):
            cur_val = flag + l1.val
            l1 = l1.next
            if cur_val >= 10:
                flag = 1
                cur_val = cur_val - 10
            else:
                flag = 0
            cur = ListNode(cur_val)
            link.next = cur
            link = link.next

        while (l2):
            cur_val = flag + l2.val
            l2 = l2.next
            if cur_val >= 10:
                flag = 1
                cur_val = cur_val - 10
            else:
                flag = 0
            cur = ListNode(cur_val)
            link.next = cur
            link = link.next

        if (flag):
            cur = ListNode(flag)
            link.next = cur

        return dummy_head.next


def list_to_linked_list(l):
  """
  将列表转换为头结点对。

  Args:
    l: 列表。

  Returns:
    头结点
  """

  # 初始化头结点。
  head = ListNode(l[0])
  p = head

  # 逐个创建链表结点。
  for i in range(1, len(l)):
    p.next = ListNode(l[i])
    p = p.next

  # 返回头结点对。
  return head

# l1_list = [9,9,9,9,9,9,9]
# l2_list = [9,9,9,9]

l1_list = [9,9,1]
l2_list = [1]
# 测试结果:[0,0,2,1]
# 	期望结果:[0,0,2]
l1 = list_to_linked_list(l1_list)
l2 = list_to_linked_list(l2_list)


Solution_sample = Solution()
res = Solution_sample.addTwoNumbers(l1,l2)

print(res)
while res:
    print(res.val)
    res = res.next

