# 给你一棵二叉树的根节点 root ，返回其节点值的 后序遍历 。
#
#
#
#  示例 1：
#
#
# 输入：root = [1,null,2,3]
# 输出：[3,2,1]
#
#
#  示例 2：
#
#
# 输入：root = []
# 输出：[]
#
#
#  示例 3：
#
#
# 输入：root = [1]
# 输出：[1]
#
#
#
#
#  提示：
#
#
#  树中节点的数目在范围 [0, 100] 内
#  -100 <= Node.val <= 100
#
#
#
#
#  进阶：递归算法很简单，你可以通过迭代算法完成吗？
#
#  Related Topics 栈 树 深度优先搜索 二叉树 👍 1177 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        stack = [root]
        stack2 = []
        res = []
        if not  root:
            return res
        while(stack):
            node = stack.pop()
            stack2.append(node)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        while(stack2):
            res.append(stack2.pop().val)

        return res
