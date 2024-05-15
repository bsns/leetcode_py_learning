# 给定一个已排序的链表的头 head ， 删除原始链表中所有重复数字的节点，只留下不同的数字 。返回 已排序的链表 。
#
#
#
#  示例 1：
#
#
# 输入：head = [1,2,3,3,4,4,5]
# 输出：[1,2,5]
#
#
#  示例 2：
#
#
# 输入：head = [1,1,1,2,3]
# 输出：[2,3]
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
#  Related Topics 链表 双指针 👍 1292 👎 0

from typing import Optional
# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:



    # [1, 2, 3, 3, 4, 4, 5]
        #    pre slow fast
        if not head:
            return head
        dummy_head = ListNode(0)
        dummy_head.next = head
        fast = head
        # fast = head.next
        pre = dummy_head
        # pre      fast
        #      [1,   2,    3, 3, 4, 4, 5]
        #           pre          fast
        while (fast):
            if (fast.next and fast.next.val == fast.val):
                slow = fast
                while(fast and fast.val == slow.val):
                    fast = fast.next

                pre.next = fast
            else:
                if(fast):
                    fast = fast.next
                    pre = pre.next

        return dummy_head.next

Solution_demo = Solution()


def build_list(nums):
    """
    根据列表 `nums` 构建链表

    Args:
        nums (list): 链表中元素的列表

    Returns:
        ListNode: 链表的头节点
    """
    head = ListNode(val=nums[0])
    cur = head
    for num in nums[1:]:
        cur.next = ListNode(val=num)
        cur = cur.next
    return head

# 测试用例
nums = [1, 2, 3, 3, 4, 4, 5]
# 测试用例:[1,2,3,3,4,4,5]
# 	测试结果:[1,2,4,5]
# 	期望结果:[1,2,5]


# nums = [1,1,1,2,3]
# # 测试用例:[1,1,1,2,3]
# # 	测试结果:[3]
# # 	期望结果:[2,3]

# nums = [1,1]
# 期望结果:[]
# # 构建链表
head = build_list(nums)

res = Solution_demo.deleteDuplicates(head)
cur = res
while cur:
    print(cur.val, end=" ")
    cur = cur.next