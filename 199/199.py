# 给定一个二叉树的 根节点 root，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。
#
#
#
#  示例 1:
#
#
#
#
# 输入: [1,2,3,null,5,null,4]
# 输出: [1,3,4]
#
#
#  示例 2:
#
#
# 输入: [1,null,3]
# 输出: [1,3]
#
#
#  示例 3:
#
#
# 输入: []
# 输出: []
#
#
#
#
#  提示:
#
#
#  二叉树的节点个数的范围是 [0,100]
#
#  -100 <= Node.val <= 100
#
#
#  Related Topics 树 深度优先搜索 广度优先搜索 二叉树 👍 961 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root):
        res = []
        stack = []

        if not root:
            return res

        stack.append(root)
        while(stack):

            tmp_last = [tmp.val for tmp in stack][-1]

            res.append(tmp_last)

            tmp_stack = []
            for tmp in stack:
                if tmp.left:
                    tmp_stack.append(tmp.left)
                if tmp.right:
                    tmp_stack.append(tmp.right)

            stack = tmp_stack

        return res

Solution_sample = Solution()
a = TreeNode(3)
b = TreeNode(9)
c = TreeNode(20)
d = TreeNode(15)
e = TreeNode(7)
a.left = b
a.right = c
c.left = d
c.right = e

res = Solution_sample.rightSideView(a)
print(res)
