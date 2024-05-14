# 给定二叉树的根节点 root ，返回所有左叶子之和。
#
#
#
#  示例 1：
#
#
#
#
# 输入: root = [3,9,20,null,null,15,7]
# 输出: 24
# 解释: 在这个二叉树中，有两个左叶子，分别是 9 和 15，所以返回 24
#
#
#  示例 2:
#
#
# 输入: root = [1]
# 输出: 0
#
#
#
#
#  提示:
#
#
#  节点数在 [1, 1000] 范围内
#  -1000 <= Node.val <= 1000
#
#
#
#
#  Related Topics 树 深度优先搜索 广度优先搜索 二叉树 👍 711 👎 0

from typing import Optional
# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 0

        leftValue = self.sumOfLeftLeaves(root.left)  # 左
        rightValue = self.sumOfLeftLeaves(root.right)  # 右

        if root.left and not root.left.left and not root.left.right:  # 左子树是左叶子的情况
            leftValue += root.left.val

        sum_val = leftValue + rightValue  # 中
        return sum_val


Solution_demo = Solution()
a= TreeNode(3)
a.left = TreeNode(9)
a.right = TreeNode(20)

a.right.left = TreeNode(15)
a.right.right = TreeNode(7)

res= Solution_demo.sumOfLeftLeaves(a)
print(res)