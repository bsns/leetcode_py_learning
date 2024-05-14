# 给定一个二叉树的 根节点 root，请找出该二叉树的 最底层 最左边 节点的值。
#
#  假设二叉树中至少有一个节点。
#
#
#
#  示例 1:
#
#
#
#
# 输入: root = [2,1,3]
# 输出: 1
#
#
#  示例 2:
#
#
#
#
# 输入: [1,2,3,4,null,5,6,null,null,7]
# 输出: 7
#
#
#
#
#  提示:
#
#
#  二叉树的节点个数的范围是 [1,10⁴]
#
#  -2³¹ <= Node.val <= 2³¹ - 1
#
#
#  Related Topics 树 深度优先搜索 广度优先搜索 二叉树 👍 575 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        q = []
        q.append(root)

        left = 0
        while(q):
            current_line = q
            tmp = []
            left = current_line[0].val
            for i in current_line:
                if i.left:
                    tmp.append(i.left)
                if i.right:
                    tmp.append(i.right)
                q = tmp

        return left
