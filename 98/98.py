# 给你一个二叉树的根节点 root ，判断其是否是一个有效的二叉搜索树。
#
#  有效 二叉搜索树定义如下：
#
#
#  节点的左子树只包含 小于 当前节点的数。
#  节点的右子树只包含 大于 当前节点的数。
#  所有左子树和右子树自身必须也是二叉搜索树。
#
#
#
#
#  示例 1：
#
#
# 输入：root = [2,1,3]
# 输出：true
#
#
#  示例 2：
#
#
# 输入：root = [5,1,4,null,null,3,6]
# 输出：false
# 解释：根节点的值是 5 ，但是右子节点的值是 4 。
#
#
#
#
#  提示：
#
#
#  树中节点数目范围在[1, 10⁴] 内
#  -2³¹ <= Node.val <= 2³¹ - 1
#
#
#  Related Topics 树 深度优先搜索 二叉搜索树 二叉树 👍 2179 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root) -> bool:

        def helper(node, lower = float('-inf'), upper = float('inf')):
            if not node:
                return True

            if node.val >= upper or node.val <= lower:
                return False

            if not helper(node.left, lower, node.val):
                return False
            if not helper(node.right, node.val, upper):
                return False
            return True

        return helper(root)



Solution_sample = Solution()
a = TreeNode(2)
b = TreeNode(2)
c = TreeNode(2)


a.left = b
a.right = c
# 测试用例:[2,2,2]
# 	测试结果:true
# 	期望结果:false


res = Solution_sample.isValidBST(a)
print(res)
