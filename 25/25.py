# 给你链表的头节点 head ，每 k 个节点一组进行翻转，请你返回修改后的链表。
#
#  k 是一个正整数，它的值小于或等于链表的长度。如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。
#
#  你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。
#
#
#
#  示例 1：
#
#
# 输入：head = [1,2,3,4,5], k = 2
# 输出：[2,1,4,3,5]
#
#
#  示例 2：
#
#
#
#
# 输入：head = [1,2,3,4,5], k = 3
# 输出：[3,2,1,4,5]
#
#
#
# 提示：
#
#
#  链表中的节点数目为 n
#  1 <= k <= n <= 5000
#  0 <= Node.val <= 1000
#
#
#
#
#  进阶：你可以设计一个只用 O(1) 额外内存空间的算法解决此问题吗？
#
#
#
#
#  Related Topics 递归 链表 👍 2167 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head, k: int):

        # head = [1,2,3,4,5], k = 2
        # 输出：[2,1,4,3,5]
        cur = head
        helper = []

        dummy_head = ListNode(0)
        new = dummy_head

        while(cur):
            tmp = cur
            for i in range(k):
                if(cur):
                    helper.append(cur)
                if(cur):
                    cur = cur.next


            if (len(helper) <k):
                new.next = tmp
                return dummy_head.next


            while helper:
                new.next = helper.pop()
                new = new.next

            new.next = cur

        return dummy_head.next


# a = ListNode(1)
# b = ListNode(2)
# c = ListNode(3)
# d = ListNode(4)
# e = ListNode(5)
# a.next = b
# b.next = c
# c.next = d
# d.next = e
# k = 2



a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)
a.next = b
b.next = c
c.next = d
d.next = e
k = 3
# 测试结果:[3,2,1,5]
# 期望结果:[3,2,1,4,5]



# a = ListNode(1)
# b = ListNode(2)
#
# a.next = b
#
# k = 2
# 测试结果:[1,2]
# 	期望结果:[2,1]

Solution_sample = Solution()
res = Solution_sample.reverseKGroup(a,k)

while(res):
    print(res.val)
    res = res.next


