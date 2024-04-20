# 给定一个二叉树，判断它是否是 平衡二叉树
#
#
#
#  示例 1：
#
#
# 输入：root = [3,9,20,null,null,15,7]
# 输出：true
#
#
#  示例 2：
#
#
# 输入：root = [1,2,2,3,3,null,null,4,4]
# 输出：false
#
#
#  示例 3：
#
#
# 输入：root = []
# 输出：true
#
#
#
#
#  提示：
#
#
#  树中的节点数在范围 [0, 5000] 内
#  -10⁴ <= Node.val <= 10⁴
#
#
#  Related Topics 树 深度优先搜索 二叉树 👍 1501 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        self.res = True
        def help(node):

            if not node:
                return 0

            left = help(node.left)+1
            right = help(node.right)+1

            if (abs(left-right)>1):
                self.res = False

            value = max(left,right)

            return value

        help(root)
        return self.res

