# 给你一棵二叉树的根节点
#  root ，请你判断这棵树是否是一棵 完全二叉树 。
#
#  在一棵 完全二叉树 中，除了最后一层外，所有层都被完全填满，并且最后一层中的所有节点都尽可能靠左。最后一层（第 h 层）中可以包含
#  1 到
#  2ʰ 个节点。
#
#
#
#  示例 1：
#
#
#
#
# 输入：root = [1,2,3,4,5,6]
# 输出：true
# 解释：最后一层前的每一层都是满的（即，节点值为 {1} 和 {2,3} 的两层），且最后一层中的所有节点（{4,5,6}）尽可能靠左。
#
#
#  示例 2：
#
#
#
#
# 输入：root = [1,2,3,4,5,null,7]
# 输出：false
# 解释：值为 7 的节点不满足条件「节点尽可能靠左」。
#
#
#
#
#  提示：
#
#
#  树中节点数目在范围 [1, 100] 内
#  1 <= Node.val <= 1000
#
#
#  Related Topics 树 广度优先搜索 二叉树 👍 273 👎 0

from typing import Optional
# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return True
        stack = []
        stack.append(root)
        continue_status = True
        while (len(stack) > 0):
            tmp_stack = []
            for item in stack:
                if item.left:
                    if not continue_status:
                        return False
                    tmp_stack.append(item.left)
                else:
                    continue_status = False

                if item.right:
                    if not continue_status:
                        return False
                    tmp_stack.append(item.right)
                else:
                    continue_status = False
            stack = tmp_stack

        return True


Solution_sample = Solution()

# a = TreeNode(1)
# b = TreeNode(2)
# c = TreeNode(3)
# d = TreeNode(4)
# e = TreeNode(5)
# f = TreeNode(6)
# a.left = b
# a.right = c
# b.left = d
# b.right = e
# c.left = f


a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)
f = TreeNode(7)
a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
# 期望结果:false


# a.right = c
res = Solution_sample.isCompleteTree(a)
print(res)