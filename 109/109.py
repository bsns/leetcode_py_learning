# 给定一个单链表的头节点 head ，其中的元素 按升序排序 ，将其转换为 平衡 二叉搜索树。
#
#
#
#  示例 1:
#
#
#
#
# 输入: head = [-10,-3,0,5,9]
# 输出: [0,-3,9,-10,null,5]
# 解释: 一个可能的答案是[0，-3,9，-10,null,5]，它表示所示的高度平衡的二叉搜索树。
#
#
#  示例 2:
#
#
# 输入: head = []
# 输出: []
#
#
#
#
#  提示:
#
#
#  head 中的节点数在[0, 2 * 10⁴] 范围内
#  -10⁵ <= Node.val <= 10⁵
#
#
#  Related Topics 树 二叉搜索树 链表 分治 二叉树 👍 895 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.
from typing import  Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:

        # 输入: head = [-10, -3, 0, 5, 9]
        # 输出: [0, -3, 9, -10, null, 5]
        #
        def helper(head,tail):
            if not head :
                return None
            # if head == tail:
            #     return TreeNode(head.val)
            if  head.next ==  None:
                return TreeNode(head.val)
            slow = fast = head

            pre = None
            while (fast != None and fast.next != None):
                fast = fast.next.next
                pre = slow
                slow = slow.next
            slow_next = slow.next
            if(pre):
                pre.next = None

            tail = fast



            root = TreeNode(slow.val)
            root.left = helper(head,pre)
            root.right = helper(slow_next,tail)

            return root

        root = helper(head,None)
        return root



def test_sorted_list_to_bst():
    # head = ListNode(-10)
    # head.next = ListNode(-3)
    # head.next.next = ListNode(0)
    # head.next.next.next = ListNode(5)
    # head.next.next.next.next = ListNode(9)

    head = ListNode(0)

    root = Solution().sortedListToBST(head)
    assert root.val == 0
    # assert root.left.val == -3
    # assert root.right.val == 9
    # assert root.left.left.val == -10
    # assert root.right.right.val == 5


test_sorted_list_to_bst()